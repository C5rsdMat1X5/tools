msg = input("Message: ")
q = int(input("Quantity: "))

c = None
while c not in [True, False]:
    c = input("Count? (y/n): ").lower() == "y"

def f():
    height = 4 if q % 2 == 0 else 3
    u = 0

    def print_msg(spaces):
        nonlocal u
        print(f"[{u}]" if c else "", " " * spaces + msg)
        u += 1

    pattern = list(range(height)) + list(range(height - 2, 0, -1))
    pattern_len = len(pattern)

    i = 1
    while u < q + 1:
        print_msg(pattern[i % pattern_len])
        i += 1

if __name__ == "__main__":
    f()