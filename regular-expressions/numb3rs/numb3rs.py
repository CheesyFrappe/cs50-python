import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^([0-9])+\.([0-9])+\.([0-9])+\.([0-9])+$", ip):
        numbers = ip.split(".")
        for number in numbers:
            if int(number) < 0 or int(number) > 255:
                return False
    else:
        return False
    return True


if __name__ == "__main__":
    main()
