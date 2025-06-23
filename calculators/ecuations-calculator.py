equ = input("Ecuation: ").replace(" ", "")
equation = []
i = 0

while i < len(equ):
    if equ[i].isdigit():
        num = equ[i]
        while i + 1 < len(equ) and equ[i + 1].isdigit():
            i += 1
            num += equ[i]
        equation.append(int(num))
    else:
        equation.append(equ[i])
    i += 1

print("Ecuations on list:", equation)

equal_idx = equation.index("=")
op_idx = None

for idx, val in enumerate(equation):
    if isinstance(val, str) and val in "+-*/":
        op_idx = idx
        break

a = equation[op_idx - 1]
b = equation[op_idx + 1]
res = equation[equal_idx + 1]
op = equation[op_idx]

if a == "x":
    if op == "+":
        x = res - b
    elif op == "-":
        x = res + b
    elif op == "*":
        x = res / b
    elif op == "/":
        x = res * b

elif b == "x":
    if op == "+":
        x = res - a
    elif op == "-":
        x = a - res
    elif op == "*":
        x = res / a
    elif op == "/":
        x = a / res

elif res == "x":
    if op == "+":
        x = a + b
    elif op == "-":
        x = a - b
    elif op == "*":
        x = a * b
    elif op == "/":
        x = a / b

print("x =", x)