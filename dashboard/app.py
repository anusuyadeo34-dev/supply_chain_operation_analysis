import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_data, calculate_kpis
from customer_analysis import show_customer_analysis
from discount_analysis import show_discount_analysis
from regional_analysis import show_regional_analysis

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="APL Profitability Dashboard",
    layout="wide"
)

# ---------------------------------------------------
# CLEAN SIDEBAR CSS
# ---------------------------------------------------

st.markdown("""
<style>

section[data-testid="stSidebar"] {
    background-color: #111827;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = load_data()

# ---------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------

st.sidebar.title("Dashboard Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Overview",
        "Customer Analysis",
        "Discount Analysis",
        "Shipping Analysis",
        "Order Status",
        "Delivery Risk",
        "Category Profitability",
        "Insights Heatmap Analysis"
    ]
)

# ---------------------------------------------------
# FILTERS
# ---------------------------------------------------

st.sidebar.title("Filters")

segment = st.sidebar.selectbox(
    "Customer Segment",
    df["Customer Segment"].dropna().unique()
)

market = st.sidebar.selectbox(
    "Market",
    df["Market"].dropna().unique()
)

filtered_df = df[
    (df["Customer Segment"] == segment) &
    (df["Market"] == market)
]

# ---------------------------------------------------
# DOWNLOAD BUTTON
# ---------------------------------------------------

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.sidebar.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)

# ---------------------------------------------------
# OVERVIEW PAGE
# ---------------------------------------------------

if page == "Overview":

    st.title("Customer, Product & Profitability Analysis")

    revenue, profit, margin = calculate_kpis(filtered_df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", f"${revenue:,.2f}")
    col2.metric("Total Profit", f"${profit:,.2f}")
    col3.metric("Profit Margin", f"{margin:.1f}%")

    # Revenue by Category

    st.subheader("Revenue by Category")

    category_sales = filtered_df.groupby(
        "Category Name"
    )["Sales"].sum().reset_index()

    fig = px.bar(
        category_sales,
        x="Category Name",
        y="Sales",
        title="Revenue by Category",
        template="plotly"
    )

    fig.update_layout(
        transition_duration=500
    )

    st.plotly_chart(fig, use_container_width=True)

    # Profit by Region

    st.subheader("Profit by Region")

    region_profit = filtered_df.groupby(
        "Order Region"
    )["Order Profit Per Order"].sum().reset_index()

    fig2 = px.bar(
        region_profit,
        x="Order Region",
        y="Order Profit Per Order",
        title="Profit by Region",
        template="plotly"
    )

    fig2.update_layout(
        transition_duration=500
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# CUSTOMER ANALYSIS
# ---------------------------------------------------

elif page == "Customer Analysis":

    show_customer_analysis(filtered_df)

# ---------------------------------------------------
# DISCOUNT ANALYSIS
# ---------------------------------------------------

elif page == "Discount Analysis":

    show_discount_analysis(filtered_df)

# ---------------------------------------------------
# SHIPPING ANALYSIS
# ---------------------------------------------------

elif page == "Shipping Analysis":

    st.title("Shipping Mode Analysis")

    shipping = filtered_df.groupby(
        "Shipping Mode"
    )["Sales"].sum().reset_index()

    fig = px.pie(
        shipping,
        names="Shipping Mode",
        values="Sales",
        title="Shipping Mode Distribution",
        template="plotly"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# ORDER STATUS
# ---------------------------------------------------

elif page == "Order Status":

    st.title("Order Status Analysis")

    status = filtered_df.groupby(
        "Order Status"
    )["Sales"].count().reset_index()

    fig = px.bar(
        status,
        x="Order Status",
        y="Sales",
        title="Order Status Count",
        template="plotly"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# DELIVERY RISK
# ---------------------------------------------------

elif page == "Delivery Risk":

    st.title("Late Delivery Risk Analysis")

    risk = filtered_df.groupby(
        "Late_delivery_risk"
    )["Sales"].count().reset_index()

    fig = px.pie(
        risk,
        names="Late_delivery_risk",
        values="Sales",
        title="Late Delivery Risk",
        template="plotly"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# CATEGORY PROFITABILITY
# ---------------------------------------------------

elif page == "Category Profitability":

    st.title("Product Category Profitability")

    category_profit = filtered_df.groupby(
        "Category Name"
    )["Order Profit Per Order"].sum().reset_index()

    fig = px.bar(
        category_profit,
        x="Category Name",
        y="Order Profit Per Order",
        title="Category Profitability",
        template="plotly"
    )

    fig.update_layout(
        transition_duration=500
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# HEATMAP ANALYSIS
# ---------------------------------------------------

elif page == "Insights Heatmap Analysis":

    st.title("Insights Heatmap Analysis")

    numeric_df = filtered_df.select_dtypes(include=['number'])

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Blues",
        title="Correlation Heatmap"
    )

    st.plotly_chart(fig, use_container_width=True)