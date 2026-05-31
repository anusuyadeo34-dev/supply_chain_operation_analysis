import streamlit as st
import plotly.express as px

def show_regional_analysis(filtered_df):

    st.title("Regional Profit Analysis")

    region_profit = filtered_df.groupby(
        "Order Region"
    )["Order Profit Per Order"].sum().reset_index()

    fig = px.bar(
        region_profit,
        x="Order Region",
        y="Order Profit Per Order",
        color="Order Profit Per Order",
        title="Profit by Region",
        template="plotly_dark"
    )

    fig.update_layout(
        transition_duration=500,
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)