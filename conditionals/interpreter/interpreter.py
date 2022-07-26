def main():
    expression = input("Expression:")
    x, y, z = expression.split(" ")

    if y == "+":
        result = (int(x) + int(z))

    if y == "-":
        result = (int(x) - int(z))

    if y == "/":
        result = (int(x) / int(z))

    if y == "*":
        result = (int(x) * int(z))

    print(f"{result:.1f}")
if __name__ == "__main__":
    main()