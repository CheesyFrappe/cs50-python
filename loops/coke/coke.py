def main():

    print("Amount due: 50")
    new_coin = 50

    while True:

        coin = int(input("Insert coin:"))

        if coin != 25 and coin != 10 and coin != 5:
            print("Amount due: 50")
            continue
        elif coin == 25 or coin == 10 or coin == 5:
            new_coin -= coin
            if new_coin < 0:
                print("Change owed:", (new_coin * -1))
                break


            if new_coin == 0:
                print("Change owed: 0")
                break
            else:
                print("Amount due: ", new_coin)



if __name__ == "__main__":
    main()