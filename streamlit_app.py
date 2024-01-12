import streamlit as st

st.title('My Parents\' New Healthy Diner')
st.header('Breakfast Menu', divider='blue')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

menu = '''Omega 3 & Blueberry Oatmeal  
Kale, Spinach, & Rocket Smoothie  
Hard-Boiled Free-Range Egg
'''
st.markdown(menu)
