import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def show_heatmap(filtered_df):

    st.subheader("Correlation Heatmap")

    numerical_df = filtered_df.select_dtypes(
        include=['float64', 'int64']
    )

    corr = numerical_df.corr()

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)