def main():
    fruit = input("Item:")
    nutritions(fruit.strip().lower())

def nutritions(s):
    nutritions = [
        {"name":"apple", "calories": 130},
        {"name": "avocado", "calories": 50},
        {"name": "banana", "calories": 110},
        {"name": "cantaloupe", "calories": 50},
        {"name": "grapefruit", "calories": 60},
        {"name": "grapes", "calories": 90},
        {"name": "honeydew melon", "calories": 50},
        {"name": "kiwifruit", "calories": 90},
        {"name": "lime", "calories": 20},
        {"name": "orange", "calories": 80},
        {"name": "lemon", "calories": 15},
        {"name": "peach", "calories": 60},
        {"name": "nectarine", "calories": 60},
        {"name": "pear", "calories": 100},
        {"name": "pineapple", "calories": 50},
        {"name": "plums", "calories": 70},
        {"name": "strawberries", "calories": 50},
        {"name": "sweet cherries", "calories": 100},
        {"name": "tangerine", "calories": 50},
        {"name": "watermelon", "calories": 80}
]
    for fruit in nutritions:
        if fruit["name"] == s:
            print("Calories:", fruit["calories"])
    else:
        return None


if __name__ == "__main__":
    main()