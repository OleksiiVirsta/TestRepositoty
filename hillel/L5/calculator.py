import operator
def calculator(num1, num2, operation):
    actions = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "//": operator.floordiv,
        "%": operator.mod,
        "**": operator.pow,
    }
    x = num1
    action = operation
    y = num2
    if y == 0.0 and action in ['/', '//', '%']:
        print('Error. Division by zero!')
    else:
        func = actions.get(action)
        if not func:
            print('Not supported action')
        else:
            return func(x, y)

assert calculator(5, 3, '+') == 8
print('OK')