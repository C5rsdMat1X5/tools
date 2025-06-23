def f(r): 
    return 1 if r == 0 else r * f(r - 1)
i = int(input("Number: "))
print("Not valid" if i < 0 else f"Factorial: {f(i)}")