import streamlit as st

my_function1 = x0 + 0.5*x1 + 0.125*x2 + 60

my_function2 = (y0 + 0.5*y1 + 0.125*y2 + 5) * c

st.title("実数値計算")

x0 = st.number_input("種族値(HP):", value=0)
x1 = st.number_input("個体値(HP):", value=0)
x2 = st.number_input("努力値(HP):", value=0)

y0 = st.number_input("種族値(A,B,C,D,S):", value=0)
y1 = st.number_input("個体値(A,B,C,D,S):", value=0)
y2 = st.number_input("努力値(A,B,C,D,S):", value=0)

c = st.sidebar.selectbox("性格補正",["1.1","1","0.9"])

st.write("実数値:")
st.write("HP: ", my_function1)
st.write("こうげき、ぼうぎょ、とくこう、とくぼう、すばやさ: ", my_function2)
