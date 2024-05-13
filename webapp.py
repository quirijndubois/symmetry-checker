import streamlit as st

from main import *

import sympy as smp
from sympy.parsing.sympy_parser import parse_expr


def dx_to_latex(latex):
    for i in range(1, n+1):
        i = n+1-i
        if i == 1:
            latex = latex.replace("dx", r"\frac{dx}{dt}")
        else:
            latex = latex.replace(
                i*"d"+"x", r"\frac{d^{"+str(i)+r"}x}{dt^{"+str(i)+r"}}")
    return latex


n = 5

st.title("Symmetry checker")

invoer = st.text_input("Input equation of motion:",value="diff(x(t),t,2)=-x(t)")

invoer = str(invoer).split("=")

if len(invoer) == 2:
    left = parse_expr(invoer[0])
    right = parse_expr(invoer[1])
else:
    raise Exception(
        "Please enter valid equation. Example: x(t)=1")

expr = left - right
expr = expr.simplify().doit()

st.write("Parsed expression: ")

expr_latex = smp.latex(expr)

expr_latex = dx_to_latex(expr_latex)

st.latex(expr_latex+"=0")

st.divider()

# time symmetry:
t_sym, t_transform = check_t_symmetry(expr)


cols = st.columns(2)
if t_sym:
    cols[0].subheader("Time reversal symmetry confirmed ✅")
else:
    cols[0].subheader("Time reversal symmetry not found ❌")

cols[1].write("Transformed form:")
t_transform = dx_to_latex(smp.latex(t_transform))+"=0"
cols[1].latex(t_transform)

st.divider()

# time translation symmetry:
t_sym, t_transform = check_t_translation(expr)


cols = st.columns(2)
if t_sym:
    cols[0].subheader("Time translation symmetry confirmed ✅")
else:
    cols[0].subheader("Time translation symmetry not found ❌")

cols[1].write("Transformed form:")
t_transform = dx_to_latex(smp.latex(t_transform))+"=0"
cols[1].latex(t_transform)

st.divider()