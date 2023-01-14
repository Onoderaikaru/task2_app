import streamlit as st

st.title("実数値計算")

num1 = st.number_input("種族値(HP):")
num2 = st.number_input("個体値(HP):")
num3= st.number_input("努力値(HP):")

num4 = st.number_input("種族値(A,B,C,D,S):")
num5 = st.number_input("個体値(A,B,C,D,S):")
num6 = st.number_input("努力値(A,B,C,D,S):")

c = st.selectbox("性格補正",["1.1","1","0.9"])

result = None
if c == "1.1":
  result1 = (num4 + 0.5*num5 + 0.125*num6 + 5) * 1.1
elif c == "1.0":
  result1 = (num4 + 0.5*num5 + 0.125*num6 + 5) * 1.0
elif c == "0.9":
  result1 = (num4 + 0.5*num5 + 0.125*num6 + 5) * 0.9

st.write("実数値:")
st.write("HP: ", result1)
