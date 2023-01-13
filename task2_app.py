import streamlit as st

def HP_function(x):
    return x[0] + 0.5*x[1] + 0.125*x[2] + 60

def ABCDS_function(y):
    return (y[0] + 0.5*y[1] + 0.125*y[2] + 5) * c

st.title("実数値計算")

x0 = st.number_input("種族値(HP):", value=0)
x1 = st.number_input("個体値(HP):", value=0)
x2 = st.number_input("努力値(HP):", value=0)

y0 = st.number_input("種族値(A,B,C,D,S):", value=0)
y1 = st.number_input("個体値(A,B,C,D,S):", value=0)
y2 = st.number_input("努力値(A,B,C,D,S):", value=0)

c = st.sidebar.selectbox("性格補正",["1.1","1","0.9"])

res1 = HP_function(x)
res2 = ABCDS_function(y)

st.write("実数値:")
st.write("HP: ", res1)
st.write("こうげき、ぼうぎょ、とくこう、とくぼう、すばやさ: ", res2)
