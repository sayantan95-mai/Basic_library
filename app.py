import streamlit as st
import pandas as pd
from src.items import Book, DVD, Magazine
from src.users import Member
from data.data import load_data, save_all_data


# --- Helper Functions ---
def get_fresh_data():
    raw_items = load_data("library_data.json")
    items = []
    for i in raw_items:
        if i['type'] == 'Book':
            obj = Book(i['title'], i['unique_id'], i['location'], i.get('pages'))
        elif i['type'] == 'DVD':
            obj = DVD(i['title'], i['unique_id'], i['location'], i.get('runtime'))
        elif i['type'] == 'Magazine':
            obj = Magazine(i['title'], i['unique_id'], i['location'], i.get('issue'))
        obj.is_borrowed = i['is_borrowed']
        items.append(obj)

    raw_members = load_data("users.json")
    users = []
    for u in raw_members:
        mem = Member(u['name'], u['user_id'])
        mem.borrowed_items = u['borrowed_items']
        users.append(mem)

    return items, users


def save_state(items, users):
    i_data = [x.to_dict() for x in items]
    u_data = [x.to_dict() for x in users]
    save_all_data("library_data.json", i_data)
    save_all_data("users.json", u_data)
    st.success("Action completed and saved!")


# --- Main App Interface ---
st.set_page_config(page_title="Library System", layout="wide")
st.title("📚 Library Management System")

library_items, members = get_fresh_data()
menu = st.sidebar.radio("Navigation", ["View Inventory", "Add Item", "Add Member", "Borrow Item", "Return Item"])

match menu:
    case "View Inventory":
        st.header("Current Inventory")
        if library_items:
            data = []
            for i in library_items:
                status = "🔴 Borrowed" if i.is_borrowed else "🟢 Available"
                data.append({"ID": i.unique_id, "Type": i.item_type, "Title": i.title, "Location": i.location,
                             "Status": status})
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No items in the library.")

    case "Add Item":
        st.header("Add New Item")
        type_choice = st.selectbox("Item Type", ["Book", "DVD", "Magazine"])

        with st.form("add_item_form"):
            title = st.text_input("Title")
            uid = st.number_input("Unique ID", min_value=1, step=1)
            loc = st.text_input("Location")

            # Dynamic input based on type
            extra = ""
            match type_choice:
                case "Book":
                    extra = st.text_input("Number of Pages")
                case "DVD":
                    extra = st.text_input("Runtime")
                case "Magazine":
                    extra = st.text_input("Issue Date")

            submitted = st.form_submit_button("Add Item")

            if submitted:
                if any(i.unique_id == uid for i in library_items):
                    st.error("Error: An item with this ID already exists.")
                else:
                    match type_choice:
                        case "Book":
                            library_items.append(Book(title, uid, loc, extra))
                        case "DVD":
                            library_items.append(DVD(title, uid, loc, extra))
                        case "Magazine":
                            library_items.append(Magazine(title, uid, loc, extra))
                    save_state(library_items, members)

    case "Add Member":
        st.header("Register New Member")
        with st.form("add_member_form"):
            name = st.text_input("Member Name")
            uid = st.number_input("User ID", min_value=1, step=1)
            submitted = st.form_submit_button("Register")

            if submitted:
                if any(m.user_id == uid for m in members):
                    st.error("Error: User ID already exists.")
                else:
                    members.append(Member(name, uid))
                    save_state(library_items, members)

    case "Borrow Item":
        st.header("Borrow an Item")
        member_opts = {f"{m.name} ({m.user_id})": m for m in members}
        selected_member_name = st.selectbox("Select Member", list(member_opts.keys()))

        avail_items = {f"{i.title} ({i.unique_id})": i for i in library_items if not i.is_borrowed}

        if not avail_items:
            st.warning("No items available to borrow.")
        else:
            selected_item_name = st.selectbox("Select Item", list(avail_items.keys()))
            if st.button("Confirm Borrow"):
                member = member_opts[selected_member_name]
                item = avail_items[selected_item_name]
                member.borrow(item.unique_id)
                item.is_borrowed = True
                save_state(library_items, members)

    case "Return Item":
        st.header("Return an Item")
        member_opts = {f"{m.name} ({m.user_id})": m for m in members}
        selected_member_name = st.selectbox("Select Member", list(member_opts.keys()))
        member = member_opts[selected_member_name]

        if not member.borrowed_items:
            st.info("This member has no borrowed items.")
        else:
            borrowed_objs = {f"{i.title} ({i.unique_id})": i for i in library_items if
                             i.unique_id in member.borrowed_items}
            selected_return_name = st.selectbox("Select Item to Return", list(borrowed_objs.keys()))
            days = st.number_input("Days kept?", min_value=1, value=1)

            if st.button("Process Return"):
                item = borrowed_objs[selected_return_name]
                member.return_item(item.unique_id)
                item.is_borrowed = False
                fine = item.calculate_fine(days)
                save_state(library_items, members)

                if fine > 0:
                    st.error(f"⚠️ OVERDUE! Fine Owed: ${fine:.2f}")
                else:
                    st.success("Returned on time. No fine.")