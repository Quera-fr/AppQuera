import streamlit as st


# Configuration de la page
st.set_page_config(
    page_title='AppWeb',
    page_icon='😎',
    layout='wide'
)

# Titre H1
st.title("Titre de la page")

st.write("Bonjour")

col1, col2 = st.columns(2)


with col1:
    input_user = st.text_input("Tape your text : ")

    st.write(input_user)


with col2:
    if st.checkbox('Show formulaire'):

        with st.form('form1'):
            age = st.selectbox('Select your age : ', range(18, 50))
            country =  st.multiselect("Select your country",
                                    ['France', 'USA'])

            if st.form_submit_button('Send'):
                st.write(age)



    with open("img.jpg", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="flower.png",
                mime="image/png"
            )

st.sidebar.image('img.jpg')