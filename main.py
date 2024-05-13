
import sympy as smp


def check_t_symmetry(expr):

    t = smp.Symbol("t")

    new_expr = smp.Subs(expr, smp.symbols("t"), -smp.symbols("t")).doit()

    # idk why sympy cannot do this, but here we apply the subsitution inside the derivatives ourselves
    for func in expr.atoms(smp.Function):
        for i in range(10):
            sign = (-1)**i
            new_expr = new_expr.replace(
                smp.Subs(smp.Derivative(func, t, i), t, -t),
                sign*smp.Derivative(func.subs(t,-t), t, i)
                )

    for func in expr.atoms(smp.Function):
        new_expr = new_expr.replace(
            func.subs(t,-t),
            func
            )

    if expr.equals(new_expr):
        return True, new_expr
    else:
        return False, new_expr


def check_t_translation(expr):

    dt = smp.Symbol("\Delta t")

    t = smp.Symbol("t")

    new_expr = smp.Subs(expr, smp.symbols("t"), t+dt).doit()

    # idk why sympy cannot do this, but here we apply the subsitution inside the derivatives ourselves
    for func in expr.atoms(smp.Function):
        for i in range(10):
            new_expr = new_expr.replace(
                smp.Subs(smp.Derivative(func, t, i), t, dt + t),
                smp.Derivative(func.subs(t,t+dt),t,i)
            )

    for func in expr.atoms(smp.Function):
        new_expr = new_expr.replace(
            func.subs(t,dt+t),
            func
            )

    if expr.equals(new_expr):
        return True, new_expr
    else:
        return False, new_expr
