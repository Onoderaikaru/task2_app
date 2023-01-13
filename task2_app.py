import streamlit as st

def my_function(x):
    return x[0] + 0.5*x[1] + 0.125*x[2] + 60

def my_function(y):
    return (y[0] + 0.5*y[1] + 0.125*y[2] + 5) * c

st.title("実数値計算")

x0 = st.number_input("種族値:", value=0)
x1 = st.number_input("個体値:", value=0)
x2 = st.number_input("努力値:", value=0)

y0 = st.number_input("種族値:", value=0)
y1 = st.number_input("個体値:", value=0)
y2 = st.number_input("努力値:", value=0)

c = sidebar.selectbox("性格補正",["1.1","1","0.9"])

res1 = my_function(x) 
res2 = my_function(y)

st.write("実数値:")
st.write("HP: ", res1)
st.write("こうげき、ぼうぎょ、とくこう、とくぼう、すばやさ: ", res2)
