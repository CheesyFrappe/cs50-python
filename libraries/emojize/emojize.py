from emoji import emojize

def main():
    emoji_input = emojize(input("Input:").strip())
    print("Output:", emoji_input)
if __name__ == "__main__":
    main()