import streamlit as st
from deta import Deta

DETA_name = "collection-key-walleye-foi"
DETA_key = "d06xvobey4w_ox37WL6krTkquwcZbhpTXTyMK9PQkV3P"

deta = Deta(DETA_key)

db = deta.Base('mydatabase')
cards_container = st.container()
#period -- incomes -- expences -- comment

def clear_txt():
    st.session_state["period"] = ""
    st.session_state["income"] = ""
    st.session_state["expence"] = ""
    st.session_state["comment"] = ""


def main():
    period = st.text_input('Period', key='period')
    incomes = st.text_input('income', key='income')
    expences = st.text_input('expence', key='expence')
    comment = st.text_area("comment", key='comment')
    
    submit_btn = st.button("submit")
    display_data()
    if submit_btn == True:
        insert_period(period, incomes, expences, comment)
        data = display_data()


def display_data():
    btn_key = 1
    data = db.fetch().items
    for data in data:
        with cards_container:
            kp = data["key"]
            st.write(data["key"])
            st.write(data["incomes"])
            st.write(data["expenses"])
            st.markdown(data["comment"])
            btn_key = btn_key+1
            update_btn = st.button("update",key=str(btn_key)+"upd")
            delete_btn = st.button("delete",key=str(btn_key)+"del")
            if delete_btn:
                delete_db(kp)
            if update_btn:
                update_db()



def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})
    st.experimental_rerun()


def update_db():
    print("hi")    


def delete_db(kp):
    db.delete(kp)
    st.experimental_rerun()


# def data_show(data):
#     btn_key = 1
#     for data in data:
#         with cards_container:
#             kp = data["key"]
#             st.write(data["key"])
#             st.write(data["incomes"])
#             st.write(data["expenses"])
#             st.markdown(data["comment"])
#             btn_key = btn_key+1
#             update_btn = st.button("update",key=str(btn_key)+"upd")

#             delete_btn = st.button("delete",key=str(btn_key)+"del")
#             if delete_btn:
#                 delete_db(kp)


if __name__ == '__main__':
    main()



# for data in data:
#   with cards_container:
#     kp = data["key"]
#     st.write(data["key"])
#     st.write(data["incomes"])
#     st.write(data["expenses"])
#     st.markdown(data["comment"])
#     btn_key = btn_key+1
#     update_btn = st.button("update",key=str(btn_key)+"upd")

#     delete_btn = st.button("delete",key=str(btn_key)+"del")
#     if delete_btn:
#         db.delete(kp)
        


# # if update_btn:


# import streamlit as st
# from deta import Deta

# # Set up Deta database
# deta = Deta('YOUR_DETA_PROJECT_KEY')
# db = deta.Base('your_database_name')

# # Streamlit app
# def main():
#     st.title('Deta Database Update')

#     # Display the current database content
#     st.header('Current Database Content:')
#     display_data()

#     # Update data form
#     st.header('Update Data:')
#     update_data()

# # Function to display current data in the database
# def display_data():
#     data = db.fetch().items
#     for item in data:
#         st.write(item)

# # Function to update data in the database
# def update_data():
#     item_id = st.text_input('Enter Item ID to Update:')
#     new_data = st.text_input('Enter New Data:')
#     if st.button('Update'):
#         if item_id and new_data:
#             # Update data in the Deta database
#             db.update({'id': item_id, 'data': new_data})
#             st.success('Data updated successfully!')
#             # Display the updated database content
#             st.header('Updated Database Content:')
#             display_data()
#         else:
#             st.warning('Please enter Item ID and New Data.')

# if __name__ == '__main__':
#     main()
