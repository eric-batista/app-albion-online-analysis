import streamlit as st
import requests

from utils.enums import ItemsEnum, CitiesEnum

import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Gathering",
    page_icon="💸",
    layout="wide"
)

st.header("Gathering Profit")

st.sidebar.title("Choose params")

if "load_state" not in st.session_state:
    st.session_state.load_state = False

if "body_infos" not in st.session_state:
    st.session_state.body_infos = []

cols = st.columns(3)

def add_info(item, quantity, city):
    st.session_state.body_infos.append({
        "name": item,
        "quantity": quantity,
        "city": city
    })

def main_scope():
    with cols[0]:
        item = st.selectbox("Select an item", ItemsEnum.list())
    with cols[1]:
        city = st.selectbox("Select a city", CitiesEnum.list())
    with cols[2]:
        quantity = st.number_input("Select quantity")

    with cols[0]:
        if st.button("Add item"):
            add_info(item, quantity, city)

    with cols[1]:
        if st.button("Remove last item"):
            st.session_state.body_infos.pop()

    resp = None

    with cols[2]:
        if st.button("Send"):
            url = 'http://localhost:8000/api-albion-accounting/accounting/gathering'
            resp = requests.post(url, json={
                "data": st.session_state.body_infos
            })

    if resp and resp.ok:
        data = resp.json()["data"]
        df_data = {
            "item": [item["name"] for item in data],
            "profit": [item["profit"] for item in data],
            "city": [item["city"] for item in data]
        }
        df = pd.DataFrame(data=df_data)
        fig = px.bar(color=df['city'], x=df['item'], y=df['profit'], barmode="group")
        st.plotly_chart(fig)
    else:
        st.table(st.session_state.body_infos)

main_scope()
