import streamlit as st
import requests

from utils.enums import ItemsEnum, CitiesEnum

import plotly.express as px

st.set_page_config(
    page_title="Market",
    page_icon="💸",
    layout="wide"
)

st.header("Market Analysis")

analyzes_type = ["", "Market history",]

st.sidebar.title("Choose params")
analysis_type = st.sidebar.selectbox("Select analysis type", analyzes_type)


if analysis_type == 'Market history':
    cols = st.columns(2)

    all_cities = st.sidebar.checkbox("Select all cities")

    with cols[0]:
        item = st.selectbox("Select an item", ItemsEnum.list())
    with cols[1]:
        city = st.selectbox("Select a city", CitiesEnum.list())

    url = 'http://localhost:8000/api-albion-accounting/accounting/items'
    resp = requests.get(url)

    if resp.ok:

        if all_cities:
            for index, city in enumerate(CitiesEnum.list()):
                if index % 2 == 0:
                    with cols[0]:
                        y = [info["lastSellPrice"] for info in resp.json() if info["name"] == item and info['city'] == city]
                        x = [info["lastPriceDate"] for info in resp.json() if info["name"] == item and info['city'] == city]
                        fig = px.area(y=y, x=x, title=f'Price history {item} - {city}')
                        fig.update_layout(
                            xaxis_title="date",
                            yaxis_title="price",
                        )
                        st.plotly_chart(fig, use_container_width=True)
                else:
                     with cols[1]:
                        y = [info["lastSellPrice"] for info in resp.json() if info["name"] == item and info['city'] == city]
                        x = [info["lastPriceDate"] for info in resp.json() if info["name"] == item and info['city'] == city]
                        fig = px.area(y=y, x=x, title=f'Price history {item} - {city}')
                        fig.update_layout(
                            xaxis_title="date",
                            yaxis_title="price",
                        )
                        st.plotly_chart(fig, use_container_width=True)
        else:
            y = [info["lastSellPrice"] for info in resp.json() if info["name"] == item and info['city'] == city]
            x = [info["lastPriceDate"] for info in resp.json() if info["name"] == item and info['city'] == city]
            fig = px.area(y=y, x=x, title=f'Price history {item} - {city}')
            fig.update_layout(
                xaxis_title="date",
                yaxis_title="price",
            )
            st.plotly_chart(fig)
