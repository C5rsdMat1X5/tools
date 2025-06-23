def calc():
    try:
        print(eval(input(":"), {"__builtins__": None}, {}))
    except Exception:
        print("An error occurred. Try again")
calc()