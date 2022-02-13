# https://pysource.com/2020/04/23/text-recognition-ocr-with-tesseract-and-opencv/
#pip install opencv-python
#pip install numpy
#pip install pytesseract
import string
import cv2
import numpy as np
import pytesseract


def IMGPOS(maptext="0:1, 2:3"):
    # [Hrizontal-offset : height,   Verticle-offset : width]
    # positionMap = "162:350, 0:1029"
    positionMap = {
        'offsetHori': int(maptext.split(", ")[0].split(":")[0]),
        'height': int(maptext.split(", ")[0].split(":")[1]),
        'offsetVert': int(maptext.split(", ")[1].split(":")[0]),
        'width': int(maptext.split(", ")[1].split(":")[1]),
    }
    return positionMap


def imgtotext(imagename: string, image_index: int = 1, positionMap="0:0, 0:0", showimage=False, printText=False):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

    # img = cv2.imread("bg.jpg")
    img = cv2.imread(imagename) 
    OBJ = IMGPOS(positionMap)
    cropped_image = img[OBJ['offsetHori']:OBJ['height'], OBJ['offsetVert']:OBJ['width']]

    # text = pytesseract.image_to_string(img)
    text = pytesseract.image_to_string(cropped_image)

    if printText:        
        print(text)
        

    if showimage:
        # cv2.imshow('Img', img)
        cv2.imshow("cropped", cropped_image)
        cv2.waitKey(0)

    return text