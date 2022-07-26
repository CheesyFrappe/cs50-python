def main():
    get_fuel = fuel()
    print(get_fuel)

def fuel():
    while True:
        try:
            fuel = input("Fraction:")
            numerator, denominator = fuel.split("/")
            if int(numerator) > int(denominator):
                continue
            if int((100 / int(denominator)) * int(numerator)) == 100 or int((100 / int(denominator)) * int(numerator)) >= 99:
                return "F"
            if int((100 / int(denominator)) * int(numerator)) == 0 or int((100 / int(denominator)) * int(numerator)) <= 1:
                return "E"
            return str(round(float(100 / int(denominator)) * int(numerator))) + "%"

        except (ValueError, ZeroDivisionError):
            pass
if __name__ == "__main__":
    main()