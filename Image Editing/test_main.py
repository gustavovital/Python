import cv2
from PIL import Image
import numpy as np

image_path = 'beach.jpeg'

def read_image(file):
    try:
        image = Image.open(file)
        return(image)
    except Exception as e:
        print(e)


image = read_image(image_path)
image.show()

img_array = np.array(image)
print(img_array)