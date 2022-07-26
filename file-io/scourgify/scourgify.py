import sys
import csv

def main():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        old_file = sys.argv[1]
        new_file = sys.argv[2]
        switch(old_file, new_file)
    except FileNotFoundError:
        sys.exit("Could not read", sys.argv[1])

def switch(old_file, new_file):
    students = []
    with open(old_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            students.append({"first": first.lstrip(), "last": last, "house": row["house"]})
    with open(new_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": 'first', "last": 'last', "house": 'house'})
        for row in students:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


if __name__ == "__main__":
    main()