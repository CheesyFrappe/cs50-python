import re
import string

def main():
    string_input = input("Input:")
    print(is_valid(string_input))


def is_valid(s):
    invalidcharacters= set(string.punctuation)
    check_number = re.search(r"\d", s)

    if len(s) > 6 or len(s) < 2:
        return False

    if " " in s:
        return False

    if not s[0].isalpha() and not s[1].isalpha():
        return False

    if check_number and s[check_number.start()] == "0":
        return False

    if check_number and re.search('[a-zA-Z]', s[check_number.start():]) and s[len(s) - 1].isdigit():
        return False

    if check_number and s[len(s) - 1].isalpha():
        return False

    if any(char in invalidcharacters for char in s):
        return False

    return True




if __name__ == "__main__":
    main()