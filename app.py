import streamlit as st
from streamlit_card import card


st.title('app')

st.subheader('event portal')
st.write("Here's our first attempt at using data to create a table:")

title = st.text_input('Movie title')

res = card(
    title="Streamlit Card",
    text="This is a test card",
    image="",
    styles={
        "card": {
            "width": "200px",
            "height": "200px",
            "border-radius": "10px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
        }
    },
)

res = card(
    key='kp',
    title="Streamlit Card",
    text="This is a test card",
    image="",
    styles={
        "card": {
            "width": "200px",
            "height": "200px",
            "border-radius": "10px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
        }
    },
)


objects = [
  {"title": "Object 1", "description": "This is object 1", "image_url": "https://example.com/image1.jpg"},
  {"title": "Object 2", "description": "This is object 2", "image_url": "https://example.com/image2.jpg"},
  {"title": "Object 3", "description": "This is object 3", "image_url": "https://example.com/image3.jpg"},
]

cards_container = st.container()

for object in objects:
  with cards_container:
    st.image(object["image_url"], width=200)
    st.header(object["title"])
    st.markdown(object["description"])