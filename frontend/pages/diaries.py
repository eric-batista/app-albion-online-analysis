import streamlit as st

st.header("Diary calculator")

empty_diary_value = st.number_input("Diary value")
filled_diary_value = st.number_input("Filled diary value")

profit = filled_diary_value - empty_diary_value

if profit > 0:
    st.success(f"{profit} silver" + f" ->  {(profit/empty_diary_value)*100:.2f} %")
else:
    st.error(f"{profit} silver" + +f" ->  {(profit/empty_diary_value)*100:.2f} %")
