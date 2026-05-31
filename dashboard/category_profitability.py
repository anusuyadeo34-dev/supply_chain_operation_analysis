import streamlit as st
import plotly.express as px

def show_category_profitability(filtered_df):

    st.subheader("Product Category Profitability")

    category_profit = (
        filtered_df.groupby("Category Name")["Order Profit Per Order"]
        .sum()
        .reset_index()
        .sort_values(by="Order Profit Per Order", ascending=False)
    )

    fig = px.bar(
        category_profit,
        x="Category Name",
        y="Order Profit Per Order",
        color="Order Profit Per Order",
        title="Profit by Product Category"
    )

    st.plotly_chart(fig, use_container_width=True)