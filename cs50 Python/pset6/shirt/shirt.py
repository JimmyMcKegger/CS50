import sys
from PIL import Image, ImageOps

def main():
    check_args()
    check_ext()

    # open file
    try:
        picture = Image.open(sys.argv[1], mode='r')
        picture_size = picture.size
    except:
        raise
        sys.exit("Input does not exist")
    # open shirt
    try:
        shirt = Image.open("shirt.png")
        picture_size = shirt.size
    except:
        raise

    # resize
    try:
        fitted_image = ImageOps.fit(
            picture, picture_size
            )
    except:
        raise

    # paste
    try:
        fitted_image.paste(shirt, shirt)
    except:
        raise

    # save
    try:
       fitted_image.save(
        sys.argv[2]
       )
    except:
        raise

def check_args():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def check_ext():
    accepted_values = (".png", ".jpeg", ".jpg")
    try:
        ext_start = sys.argv[1].index(".")
        fiile_ext = sys.argv[1][ext_start:]
    except:
        raise
    if fiile_ext not in sys.argv[2]:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()