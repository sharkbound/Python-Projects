import re
import requests
import sys
from PIL import Image, ImageDraw

edited_img_path = '../files/good_edited.jpg'
base_img_path = '../files/good.jpg'

# user: huge
# pass: file
if __name__ == '__main__':
    with open('../files/challenge9.html') as f:
        text = f.read().replace('\n', '')

    text_list = re.findall('first:\s*[0-9,]*|second:\s*[0-9,]*', text)

    first = [int(i) for i in re.findall('([0-9]{3})', text_list[0])]
    second =  [int(i) for i in re.findall('([0-9]{3})', text_list[1])]
    merged = first+second

    new_image = Image.new('RGB', (640, 840))

    for i in range(0, len(merged)-1, 2):
        x,y = merged[i], merged[i+1]
        new_image.putpixel((x,y), (255,255,255))

    new_image.save(edited_img_path)

