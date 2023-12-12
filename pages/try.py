import streamlit as st

# Define some data
cards = [{
  "title": "Object 1",
  "description": "This is object 1",
  "image_url": "https://example.com/image1.jpg",
  "id": 1,
},
{
  "title": "Object 2",
  "description": "This is object 2",
  "image_url": "https://example.com/image2.jpg",
  "id": 2,
}]

# Create a container for the cards
cards_container = st.container()

# Create a form for adding new cards
add_card_form = st.form(key="add_card_form")
add_card_title = add_card_form.text_input("Title")
add_card_description = add_card_form.text_area("Description")
add_card_image_url = add_card_form.text_input("Image URL")
add_submitted = add_card_form.form_submit_button("Add Card")

# Create a form for updating existing cards
update_card_form = st.form(key="update_card_form")
update_card_id = update_card_form.selectbox("Select Card", [str(card["id"]) for card in cards])
update_card_title = update_card_form.text_input("Title", value=cards[int(update_card_id) - 1]["title"])
update_card_description = update_card_form.text_area("Description", value=cards[int(update_card_id) - 1]["description"])
update_card_image_url = update_card_form.text_input("Image URL", value=cards[int(update_card_id) - 1]["image_url"])
update_submitted = update_card_form.form_submit_button("Update Card")

# Create a button for deleting cards
delete_button = st.button("Delete Card")

# Handle form submissions
if add_submitted:
  cards.append({
    "title": add_card_title,
    "description": add_card_description,
    "image_url": add_card_image_url,
    "id": len(cards) + 1,
  })
  st.success("Card added successfully!")

if update_submitted:
  cards[int(update_card_id) - 1] = {
    "title": update_card_title,
    "description": update_card_description,
    "image_url": update_card_image_url,
  }
  st.success("Card updated successfully!")

if delete_button:
  if len(cards) > 0:
    cards.pop()
    st.success("Card deleted successfully!")

# Display the cards
for card in cards:
  with cards_container:
    st.image(card["image_url"], width=200)
    st.header(card["title"])
    st.markdown(card["description"])
