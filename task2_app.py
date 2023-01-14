import streamlit as st

st.title("実数値計算")

A = st.number_input("種族値(HP):", value=0)
B = st.number_input("個体値(HP):", value=0)
C = st.number_input("努力値(HP):", value=0)

D = st.number_input("種族値(A,B,C,D,S):", value=0)
E = st.number_input("個体値(A,B,C,D,S):", value=0)
F = st.number_input("努力値(A,B,C,D,S):", value=0)

c = st.selectbox("性格補正",["1.1","1","0.9"])

result = None
if c == "1.1":
  result1 = A + 0.5*B + 0.125*C+ 60, result2 = (D + 0.5*E + 0.125*F + 5) * 1.1
elif c == "1.0":
  result1 = A + 0.5*B + 0.125*C+ 60, result2 = (D + 0.5*E + 0.125*F + 5) * 1.0
elif c == "0.9":
  result1 = A + 0.5*B + 0.125*C+ 60, result2 = (D + 0.5*E + 0.125*F + 5) * 0.9

st.write("実数値:")
st.write("HP: ", result1)
st.write("こうげき、ぼうぎょ、とくこう、とくぼう、すばやさ: ", result2)
