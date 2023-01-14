import streamlit as st

def my_function(x):
  return x[0] + x[1]*0.5 + x[2]*0.125+ 60

def my_function(y):
  return (y[0] + y[1]*0.5 + y[2]*0.125 + 5) * c

st.title("実数値計算")

x0 = st.number_input("種族値(HP):", value=0)
x1 = st.number_input("個体値(HP):", value=0)
x2 = st.number_input("努力値(HP):", value=0)

y0 = st.number_input("種族値(A,B,C,D,S):", value=0)
y1 = st.number_input("個体値(A,B,C,D,S):", value=0)
y2 = st.number_input("努力値(A,B,C,D,S):", value=0)

c = st.sidebar.selectbox("性格補正",["1.1","1","0.9"])

st.write("実数値:")
st.write("HP: ", my_function(x))
st.write("こうげき、ぼうぎょ、とくこう、とくぼう、すばやさ: ", my_function(y))
