import streamlit as st
import pandas as pd
import plotly.express as px

def show_customer_analysis(filtered_df):

    st.title("Top 10 Customers by Profit")

    # Correct column name
    customer_profit = filtered_df.groupby(
        "Customer Id"
    )["Order Profit Per Order"].sum().reset_index()

    customer_profit = customer_profit.sort_values(
        by="Order Profit Per Order",
        ascending=False
    ).head(10)

    fig = px.bar(
        customer_profit,
        x="Customer Id",
        y="Order Profit Per Order",
        color="Order Profit Per Order",
        title="Top 10 Customers by Profit",
        template="plotly_dark"
    )

    fig.update_layout(
        transition_duration=500,
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)