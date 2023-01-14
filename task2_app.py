import streamlit as st

st.title("実数値計算")

x0 = st.number_input("種族値(HP):", value=0)
x1 = st.number_input("個体値(HP):", value=0)
x2 = st.number_input("努力値(HP):", value=0)

y0 = st.number_input("種族値(A,B,C,D,S):", value=0)
y1 = st.number_input("個体値(A,B,C,D,S):", value=0)
y2 = st.number_input("努力値(A,B,C,D,S):", value=0)

c = st.selectbox("性格補正",["1.1","1","0.9"])

if c == "1.1":
  result1 = x0 + 0.5*x1 + 0.125*x2+ 60, result2 = (y0 + 0.5*y1 + 0.125*y2 + 5) * 1.1
elif c == "1.0":
  result1 = x0 + 0.5*x1 + 0.125*x2+ 60, result2 = (y0 + 0.5*y1 + 0.125*y2 + 5) * 1.0
elif c == "0.9":
  result1 = x0 + 0.5*x1 + 0.125*x2+ 60, result2 = (y0 + 0.5*y1 + 0.125*y2 + 5) * 0.9

st.write("実数値:")
st.write("HP: ", result1)
st.write("こうげき、ぼうぎょ、とくこう、とくぼう、すばやさ: ", result2)
