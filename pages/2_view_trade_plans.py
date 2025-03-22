import streamlit as st
import pandas as pd

def display_trading_plan():
    """
    Reads the trading_plan.csv file and displays its contents in a Streamlit app.
    """
    st.header("Trading Plan Details")

    try:
        df = pd.read_csv("trading_plan.csv")

        # Display the DataFrame in a more readable format
        for col in df.columns:
            st.subheader(col)
            st.write(df[col].iloc[0])  # Display the first row's value for each column
            st.markdown("---")  # Add a separator between columns

    except FileNotFoundError:
        st.error("Trading plan file not found. Please save a trading plan first.")
    except pd.errors.EmptyDataError:
        st.warning("The trading plan file is empty.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    display_trading_plan()