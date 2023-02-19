import streamlit as st

st.header("Accounting")

items_list = []

items_number = st.number_input("Item number")
item_value = st.number_input("Item value")

total = item_value * items_number


st.write(total)
