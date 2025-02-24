import streamlit as st

# App ka Title
st.title("Simple Calculator")

# User Inputs
num1 = st.number_input("Enter first number", value=0, step=1)
num2 = st.number_input("Enter second number", value=0, step=1)

# Operation Select Karne Ke Liye Dropdown
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculation Logic
result = None

if operation == "Addition":
    result = int(num1 + num2)
elif operation == "Subtraction":
    result = int(num1 - num2)
elif operation == "Multiplication":
    result = int(num1 * num2)
elif operation == "Division":
    if num2 != 0:
        result = int(num1 / num2)  # Integer division
    else:
        st.error("Error: Division by zero is not allowed!")

# Result Show Karna
if result is not None:
    st.success(f"Result: {result}")
