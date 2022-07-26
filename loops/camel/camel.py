def main():
    string = input("Text:")
    print(snake_case(string))

def snake_case(string):

    for i in range(len(string)):
        if string[i].isupper():
            string = string[0:i] + "_" + string[i].lower() + string[i + 1:len(string)]
    return string


if __name__== "__main__":
    main()