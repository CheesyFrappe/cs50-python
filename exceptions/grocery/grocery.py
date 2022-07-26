def main():
     list()

def list():
    grocery_list = {}
    while True:
        try:
            item = input()
        except EOFError:
            break
        # checks if item is already in list
        if item.upper() in grocery_list:
            grocery_list[item.upper()] += 1
        # if item is not in list, then adds the item in list
        else:
            grocery_list[item.upper()] = 1

    for item in sorted(grocery_list.keys()):
        print(grocery_list[item], item)

if __name__ == "__main__":
    main()