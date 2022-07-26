def main():
    question = input("Input:")
    print(twttr(question))

def twttr(user_input):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for char in user_input:
        if char in vowels:
            user_input = user_input.replace(char, "")

    return user_input


if __name__ == "__main__":
    main()