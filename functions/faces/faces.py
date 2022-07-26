def main():
    string = input("")
    convert(string)

def convert(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    print(string)

if __name__ == "__main__":
    main()