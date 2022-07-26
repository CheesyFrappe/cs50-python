from tabulate import tabulate
import sys
import csv

def main():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        user_file = sys.argv[1]
        print(menu(user_file))
    except FileNotFoundError:
        sys.exit("File does not exist")

def menu(user_file):
    pizza_menu = []
    with open(user_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pizza_menu.append(row)

    print(tabulate(pizza_menu, headers = "firstrow", tablefmt="grid"))



if __name__ == "__main__":
    main()