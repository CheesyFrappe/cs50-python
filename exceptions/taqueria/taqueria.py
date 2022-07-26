def main():
    order = get_order()

def get_order():

    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    try:
        total_amount = 0
        while True:
            order = input("Item:")
            if order.title() in menu:
                total_amount += float(menu[order.title()])
                print(f"Total: ${total_amount:.2f}")
            if order == "":
                break
    except EOFError:
        pass

if __name__ == "__main__":
    main()