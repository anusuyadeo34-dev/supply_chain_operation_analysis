import streamlit as st
import plotly.express as px

def show_discount_analysis(filtered_df):

    st.subheader("Discount vs Profit Analysis")

    fig = px.scatter(
        filtered_df,
        x="Order Item Discount",
        y="Order Profit Per Order",
        color="Order Profit Per Order",
        title="Discount vs Profit",
        hover_data=["Category Name"]
    )

    fig.update_layout(
        transition_duration=500
    )

    st.plotly_chart(fig, use_container_width=True)
