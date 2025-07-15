import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

def format_inr(value):
    """Format number to Indian currency format with ₹ symbol"""
    return "₹{:,.2f}".format(value).replace(",", "X").replace(".", ",").replace("X", ",")

st.title("Home Loan EMI Calculator ")

st.write("### Enter Home Loan Details")
col1, col2 = st.columns(2)
home_value = col1.number_input("Home Value (₹)", min_value=0, value=5000000)  # Default ₹50L
deposit = col1.number_input("Down Payment (₹)", min_value=0, value=1000000)  # Default ₹10L
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=8.5)  # Indian avg
loan_term = col2.number_input("Loan Tenure (in years)", min_value=1, value=20)

# EMI Calculation
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

# Totals
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### EMI Details")
col1, col2, col3 = st.columns(3)
col1.metric(label="Monthly EMI", value=format_inr(monthly_payment))
col2.metric(label="Total Payment", value=format_inr(total_payments))
col3.metric(label="Total Interest", value=format_inr(total_interest))

# Payment Schedule
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)
    schedule.append([i, monthly_payment, principal_payment, interest_payment, remaining_balance, year])

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

# Chart
st.write("### Year-wise Loan Balance")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)