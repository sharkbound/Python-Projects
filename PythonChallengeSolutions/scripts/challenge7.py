import os
from PIL import Image
import requests


def download_challenge7_image(img_path):
    if not os.path.exists(img_path):
        image_req = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png', stream=True)

        with open(img_path, 'wb') as img_file:
            for chunk in image_req.iter_content(chunk_size=1024):
                if chunk:  # ignore keep-alive chunks
                    img_file.write(chunk)


def main_func():
    #  Fetch the image file from the challenge page
    download_challenge7_image('../files/oxygen.png')

    img_path = '../files/oxygen.png'
    im = Image.open(open(img_path, 'rb'))
    pix = im.load()

    result = [chr(pix[i*7, 47][0]) for i in range(87)] # iterate over each gray bar area,

    print(''.join(result))  # result = smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]


if __name__ == '__main__':
    main_func()
