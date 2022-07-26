from PIL import Image, ImageOps
import sys

def main():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    input_photo = sys.argv[1]
    output_photo = sys.argv[2]

    if check_extensions(input_photo, output_photo):
        try:
            image_file = Image.open(input_photo)
        except:
            sys.exit("Input does not exist")

        shirt = Image.open("shirt.png")
        size = shirt.size
        muppet = ImageOps.fit(image_file, size)
        muppet.paste(shirt, shirt)
        muppet.save(output_photo)


def check_extensions(input_photo, output_photo):
    extension = [".jpg", ".jpeg", ".png"]
    for i in range(3):
        if input_photo.lower().endswith(extension[i]):
            for j in range(3):
                if output_photo.lower().endswith(extension[j]):
                    if extension[i] == extension[j]:
                        return True
                    else:
                        sys.exit("Input and output have different extensions")

    return False

if __name__ == "__main__":
    main()