def main():
    greet = input("Greeting:")
    print(greeting(greet.strip()))

def greeting(greet):
    if greet.startswith("Hello"):
        return "$0"
    elif greet.startswith("H"):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()