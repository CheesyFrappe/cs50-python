import sys

def main():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        user_file = sys.argv[1]
        print(loc(user_file))
    except FileNotFoundError:
        sys.exit("File does not exist")

def loc(user_file):
    count = 0
    with open(user_file, "r") as user_file:
        for line in user_file:
            if line.isspace() or line.lstrip().startswith("#"):
                continue
            else:
                count += 1
    return count

if __name__ == "__main__":
    main()