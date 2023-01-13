import streamlit as st
from scipy.optimize import linprog

st.title("線形最適化問題のソルバー")

# 目的関数を定義
c = st.text_input("目的関数 (c)", "1, 1")
c = list(map(float, c.split(",")))

# 制約条件を定義
A = st.text_input("制約条件 (A)", "1, 1\n1, 0")
A = [list(map(float, row.split(","))) for row in A.split("\n")]

b = st.text_input("制約条件 (b)", "1, 1")
b = list(map(float, b.split(",")))

# 制約条件を定義
x0_bnds = st.text_input("制約条件 (x0)", "0, None")
x0_bnds = tuple(map(float, x0_bnds.split(",")))

# 線形最適化問題を解く
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bnds])

# 結果を表示
if res.success:
    st.success("最適解が見つかりました")
    st.write("x = ", res.x)
    st.write("最適解の値 = ", res.fun)
else:
    st.error("最適解が見つかりませんでした")
