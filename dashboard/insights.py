import streamlit as st

def show_insights(filtered_df):

    st.subheader("Business Insights")

    # Highest Profit Category
    top_category = (
        filtered_df.groupby("Category Name")["Order Profit Per Order"]
        .sum()
        .idxmax()
    )

    # Highest Revenue Market
    top_market = (
        filtered_df.groupby("Market")["Sales"]
        .sum()
        .idxmax()
    )

    # Highest Profit Shipping Mode
    top_shipping = (
        filtered_df.groupby("Shipping Mode")["Order Profit Per Order"]
        .sum()
        .idxmax()
    )

    # Average Discount
    avg_discount = round(
        filtered_df["Order Item Discount"].mean(),
        2
    )

    st.success(
        f"Highest profitable category is: {top_category}"
    )

    st.info(
        f"Highest revenue market is: {top_market}"
    )

    st.warning(
        f"Most profitable shipping mode is: {top_shipping}"
    )

    st.error(
        f"Average discount provided: {avg_discount}"
    )