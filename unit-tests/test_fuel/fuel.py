def main():
    get_fuel = input("Input:")
    percentage = convert(get_fuel)

    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split("/")
            num = int(numerator)
            den = int(denominator)
            if num / den <= 1:
                return int((num / den) * 100)
            else:
                fraction = input("Input:")
                pass
        except (ValueError, ZeroDivisionError):
            raise



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()