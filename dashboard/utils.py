import pandas as pd

def load_data():

    file_path = "data/APL_Logistics.csv"

    df = pd.read_csv(
        file_path,
        encoding="latin1"
    )

    return df


def calculate_kpis(df):

    revenue = pd.to_numeric(
        df["Sales"],
        errors="coerce"
    ).sum()

    profit = pd.to_numeric(
        df["Order Profit Per Order"],
        errors="coerce"
    ).sum()

    margin = (profit / revenue) * 100

    return revenue, profit, margin