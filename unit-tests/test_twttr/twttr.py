def main():
    twitter_input = input("Input:")
    print(shorten(twitter_input))


def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for char in word:
        if char in vowels:
            word = word.replace(char, "")

    return word


if __name__ == "__main__":
    main()