
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

    if expr.equals(new_expr) or smp.Subs(new_expr,expr,0).equals(0):
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

    if expr.equals(new_expr) or smp.Subs(new_expr,expr,0).equals(0):
        return True, new_expr
    else:
        return False, new_expr
    
def check_x_translation(expr):
    dx = smp.Symbol("\Delta x")

    x = smp.Function("x")
    t = smp.Symbol("t")

    new_expr = smp.Subs(expr, x(t), x(t)+dx).doit()

    if expr.equals(new_expr) or smp.Subs(new_expr,expr,0).equals(0):
        return True, new_expr
    else:
        return False, new_expr

def check_parity(expr):
    dx = smp.Symbol("\Delta x")

    x = smp.Function("x")
    t = smp.Symbol("t")

    new_expr = smp.Subs(expr, x(t), -x(t)).doit()

    if expr.equals(new_expr) or smp.Subs(new_expr,expr,0).equals(0):
        return True, new_expr
    else:
        return False, new_expr
    
def check_boost(expr):
    dx = smp.Symbol("\Delta x")

    x = smp.Function("x")
    t = smp.Symbol("t")
    v = smp.Symbol("v")

    new_expr = smp.Subs(expr, x(t), x(t)+v*t).doit()

    if expr.equals(new_expr) or smp.Subs(new_expr,expr,0).equals(0):
        return True, new_expr
    else:
        return False, new_expr