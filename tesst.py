from sympy import symbols, Function, Subs, Derivative

t = symbols('t')
x = Function('x')

# Original derivative
original_derivative = Derivative(x(t), t)

# Apply the substitution
substituted_expression = Subs(original_derivative, t, -t)

# Simplify the substituted expression
simplified_expression = substituted_expression.doit()

print(simplified_expression)
