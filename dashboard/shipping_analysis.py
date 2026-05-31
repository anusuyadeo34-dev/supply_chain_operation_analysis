import streamlit as st
import plotly.express as px

def show_shipping_analysis(filtered_df):

    st.subheader("Shipping Mode Analysis")

    shipping_sales = (
        filtered_df.groupby("Shipping Mode")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        shipping_sales,
        x="Shipping Mode",
        y="Sales",
        color="Sales",
        title="Sales by Shipping Mode"
    )

    st.plotly_chart(fig, use_container_width=True)