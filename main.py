import streamlit as st
from PIL import Image
import streamlit_authenticator as stauth
import os
# from dotenv import load_dotenv
# load_dotenv()

# un = os.getenv("USERNAME")
# name = os.getenv("NAME")
# password = os.getenv("PASSWORD")

un = st.secrets["USERNAME"]
name = st.secrets["NAME"]
password = st.secrets["PASSWORD"]

credentials = {"usernames":{
                    un:{
                    "name":name,
                    "password":password}}}

# Create Auth Object
authenticator = stauth.Authenticate(credentials, "happy_fathers_day", "abcdef", cookie_expiry_days=30, preauthorized=['secret@gmail.com'])
name, authentication_status, username = authenticator.login('Login', 'main')

def main():
    html_code = '''
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: #F6F6F6; font-family: 'Arial', sans-serif;">Happy Father's Day!</h1>
        <p style="color: #F6F6F6; font-size: 30px; font-family: 'Arial', sans-serif;">Wishing you an amazing Fathers Day Pops </p>
        <p style="color: #F6F6F6; font-size: 20px; font-family: 'Arial', sans-serif;">from your immature sons &#128514 - Rahul and Rithik</p>
    </div>
    '''

    st.markdown(html_code, unsafe_allow_html=True)

    # for i in parts:
    #     carousel = st.container()
    #     part_path = "images/" + i
    #     images = [part_path + "/" + f for f in os.listdir(part_path)]
    #     with carousel:
    #         for image_path in images:
    #             image = Image.open(image_path)
    #             st.image(image, use_column_width=True)

    parts = os.listdir("images/")
    images = []
    col1,col2,col3 = st.columns(3)
    for i in parts:
        part_path = "images/" + i
        images += [part_path + "/" + f for f in os.listdir(part_path)].sort()

    for i, image_path in enumerate(images):
        image = Image.open(image_path)
        if i%3 == 0:
            with col1:
                st.image(image, use_column_width=True)
        elif i%3 == 1:
            with col2:
                st.image(image, use_column_width=True)
        else:
            with col3:
                st.image(image, use_column_width=True)

if authentication_status:
    # authenticator.logout('Logout', 'main', key='hi')
    main()
    # authenticator.logout('Logout', 'sidebar')
    
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')


