import streamlit as st
import plotly.express as px

def show_delivery_analysis(filtered_df):

    st.subheader("Late Delivery Risk Analysis")

    delivery_risk = (
        filtered_df.groupby("Late_delivery_risk")["Sales"]
        .count()
        .reset_index()
    )

    delivery_risk["Late_delivery_risk"] = delivery_risk[
        "Late_delivery_risk"
    ].replace({
        0: "No Risk",
        1: "Late Delivery Risk"
    })

    fig = px.pie(
        delivery_risk,
        names="Late_delivery_risk",
        values="Sales",
        title="Late Delivery Risk Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)