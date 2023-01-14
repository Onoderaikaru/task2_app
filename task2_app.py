import streamlit as st

st.title("実数値計算(Lv50,個体値31固定)")

num1 = st.number_input("種族値(HP):",value=0)
num2= st.number_input("努力値(HP):",value=0)

num3 = st.number_input("種族値(A,B,C,D,S):",value=0)
num4 = st.number_input("努力値(A,B,C,D,S):",value=0)

c = st.sidebar.selectbox("性格補正",["選択なし","1.1","1","0.9"])

if c == "選択なし":
  result1 = 0
  result2 = 0
elif c == "1.1":
  result1 = num1 + 0.5*31 + 0.125*num2+ 60
  result2 = (num3 + 0.5*31 + 0.125*num4 + 5) * 1.1
elif c == "1.0":
  result1 = num1 + 0.5*31 + 0.125*num2+ 60
  result2 = (num3 + 0.5*31 + 0.125*num4 + 5) * 1.0
elif c == "0.9":
  result1 = num1 + 0.5*31 + 0.125*num2+ 60
  result2 = (num3 + 0.5*31 + 0.125*num4 + 5) * 0.9

st.write("実数値:")
st.write("HP: ", result1)
st.write("こうげき、ぼうぎょ、とくこう、とくぼう、すばやさ: ", result2)
