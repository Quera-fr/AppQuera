import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title='Historique',
    page_icon='😎',
    layout='wide'
)


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)