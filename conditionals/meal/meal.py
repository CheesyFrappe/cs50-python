def main():
    time = input("Meal Time:")

    converted_time = float(convert(time.strip()))

    if converted_time >= 7.0 and converted_time <= 8.0:
        print("breakfast time")

    if converted_time >= 12.0 and converted_time <= 13.0:
        print("lunch time")

    if converted_time >= 18.0 and converted_time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return hours + "." + minutes


if __name__ == "__main__":
    main()