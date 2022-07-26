import random
import sys

def main():
    while True:
        try:
            level = int(input("Level:"))
            if level < 1:
                continue
            break
        except ValueError:
            pass

    random_number = random.randint(1,int(level))

    while True:
        try:
            guess_number = int(input("Guess:"))

            if guess_number > level or guess_number < 1:
                continue
            if guess_number == random_number:
                sys.exit("Just right!")
            if guess_number > random_number:
                print("Too large!")
                continue
            if guess_number < random_number:
                print("Too small!")
                continue
            break
        except ValueError:
            pass

if __name__ == "__main__":
    main()