def main():

    answer = input("What is the answer to the Great Question of Life, the Universe and Everything?")
    answer = answer.strip()

    if answer.isnumeric() and int(answer) != 42:
        print("No")
    elif not answer.isnumeric() and answer.lower() != "forty-two" and answer.lower() != "forty two":
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()