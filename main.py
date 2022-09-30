import requests

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

get_avatar = lambda avatar_link : Image.open(BytesIO(requests.get(avatar_link).content)).resize((1280, 1280)).crop((0, 300, 1280, 1280))

def main(username, avatar_link):
    avatar = get_avatar(avatar_link)
    font = ImageFont.truetype("font.ttf", 100)
    template = Image.open('template.png').convert('RGBA')
    draw = ImageDraw.Draw(template)

    draw.text((template.size[0] / 2 - font.getlength(username) / 2, 250), username, (0, 0, 0), font=font)
    template.paste(avatar, (0, 500 - 3))

    template.save('output.png')

if __name__ == '__main__':
    username = input("Username: ")
    avatar_link = input("Image link: ")

    main(username, avatar_link)

    print("Done! Saved as output.png")