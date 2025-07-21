import time

USE_COLORS = True

class Colors:
    if USE_COLORS:
        RED = "\033[31m"
        GREEN = "\033[32m"
        RESET = "\033[0m"
    else:
        RED = ""
        GREEN = ""
        RESET = ""

    @staticmethod
    def red(text):
        return f"{Colors.RED}{text}{Colors.RESET}"

    @staticmethod
    def green(text):
        return f"{Colors.GREEN}{text}{Colors.RESET}"

pattern = input(Colors.green("Name: "))
counter = 0
scale = 1

for y in range(int(15 / scale), int(-15 / scale), -1):
    for x in range(int(-30 / scale), int(30 / scale)):
        x_coord = x * 0.04 * scale
        y_coord = y * 0.1 * scale
        value = (x_coord**2 + y_coord**2 - 1) ** 3 - x_coord**2 * y_coord**3
        if value <= 0:
            char = Colors.red(pattern[counter % len(pattern)])
            print(char, end="", flush=True)
            counter += 1
        else:
            print(" ", end="", flush=True)
        time.sleep(0.001)
    print()