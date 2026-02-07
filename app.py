import streamlit as st
import pandas as pd
from datetime import datetime

# 1. App Title
st.title("💸 My Personal Finance Tracker")

# 2. Input Form
with st.form("entry_form"):
    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    category = st.selectbox("Category", ["Food", "Rent", "Transport", "Fun", "Savings"])
    notes = st.text_input("Notes")
    submitted = st.form_submit_button("Save Transaction")

    if submitted:
        # Create a new row of data
        new_data = pd.DataFrame([{
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Category": category,
            "Amount": amount,
            "Notes": notes
        }])
        
        # Here we would append to Google Sheets
        st.success(f"Saved ${amount} for {category}!")

# 3. View History
st.subheader("Recent Spending")
# This would pull from your Google Sheet
# st.dataframe(df)
