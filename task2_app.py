import streamlit as st

st.title("My Calculator App")

num1 = st.number_input("Enter a number:")
num2 = st.number_input("Enter another number:")

operation = st.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

result = None
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    result = num1 / num2

st.write("The result is:", result)
