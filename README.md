# Mortgage-Calculator

An interactive web application built with Streamlit to help you calculate monthly EMIs, total payment, and total interest on a home loan .

---

## Features

- Calculates Monthly EMI based on Home Value, Down Payment, Interest Rate, and Loan Tenure
- Displays Total Payment and Total Interest Payable
- Interactive chart showing Year-wise Remaining Loan Balance
- Formats all currency in Indian Rupee (₹)
- Generates a complete amortization schedule (principal + interest breakdown)
- Smart defaults for quick testing (e.g. ₹50L home, ₹10L deposit, 8.5% interest)

---

## Demo

<img width="1328" height="988" alt="image" src="https://github.com/user-attachments/assets/25a04587-17b7-4522-a956-4d817428e05e" />
<img width="1169" height="716" alt="image" src="https://github.com/user-attachments/assets/c787ec86-419c-43c8-a2fb-f701638d83e4" />



---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/prakirtibista/Mortgage-Calculator.git
cd Mortgage-Calculator
```

## Tech Stack

1. Python
2. Streamlit – Web framework for data apps
3. Pandas – Data manipulation
4. Matplotlib – Plotting
5. Math – EMI calculations

## Formula Used

  EMI = [P × R × (1+R)^N] / [(1+R)^N – 1]
  Where:
  P = Loan Amount
  R = Monthly Interest Rate
  N = Total Number of Payments (in months)

