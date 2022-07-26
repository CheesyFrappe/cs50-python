import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level < 1 or level > 3:
                continue
            return level
        except:
            pass


def generate_integer(level):
    score = 0

    for _ in range(10):
        tries = 0

        if level == 1:
            rand_num1 = random.randint(0,9)
            rand_num2 = random.randint(0,9)
        elif level == 2:
            rand_num1 = random.randint(10,99)
            rand_num2 = random.randint(10,99)
        else:
            rand_num1 = random.randint(100,999)
            rand_num2 = random.randint(100,999)

        while True:
            try:
                if tries == 3:
                    print(str(rand_num1) + " + " + str(rand_num2) + " = " + str(rand_num1 + rand_num2))
                    break
                answer = int(input(str(rand_num1) + " + " + str(rand_num2) + " = "))
                if answer != rand_num1 + rand_num2:
                    tries += 1
                    print("EEE")
                else:
                    score += 1
                    break
            except (EOFError, ValueError):
                pass
    print("Score: ", score)




if __name__ == "__main__":
    main()