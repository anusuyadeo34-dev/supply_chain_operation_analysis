import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Product & Category Analysis')

# Load Data

df = pd.read_csv('../data/APL_Logistics.csv')

# Category Profitability

category_profit = df.groupby('Category Name')['Order Profit Per Order'].sum().reset_index()

st.subheader('Category Profitability')

fig = px.bar(
    category_profit,
    x='Category Name',
    y='Order Profit Per Order',
    color='Category Name'
)

st.plotly_chart(fig, use_container_width=True)

# Top Products

product_profit = df.groupby('Product Name')['Order Profit Per Order'].sum().reset_index()

product_profit = product_profit.sort_values(
    by='Order Profit Per Order',
    ascending=False
)

st.subheader('Top Profitable Products')

fig2 = px.bar(
    product_profit.head(10),
    x='Product Name',
    y='Order Profit Per Order'
)

st.plotly_chart(fig2, use_container_width=True)