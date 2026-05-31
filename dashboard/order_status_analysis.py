import streamlit as st
import plotly.express as px

def show_order_status_analysis(filtered_df):

    st.subheader("Order Status Analysis")

    order_status = (
        filtered_df.groupby("Order Status")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        order_status,
        names="Order Status",
        values="Sales",
        title="Sales Distribution by Order Status"
    )

    st.plotly_chart(fig, use_container_width=True)