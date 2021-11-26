from PIL import Image
import numpy as np


def GetGreyPixels(stepWidth, mozeSize, stepHeight, graid, img, greyscale):
    for x in range(stepWidth, stepWidth + mozeSize):
        for y in range(stepHeight, stepHeight + mozeSize):
            for z in range(0, 3):
                img[x][y][z] = int(greyscale // graid) * graid

            return img


def GetGreyAverage(stepWidth, mozeSize, stepHeight, img):
    segment = img[stepWidth:stepWidth + mozeSize,
              stepHeight:stepHeight + mozeSize]
    result = np.sum(segment)
    return int(result // (3 * (mozeSize ** 2)))


def GetMosaic(graid, width, height, mozeSize, img):
    stepWidth = 0
    while stepWidth < width:
        stepHeight = 0
        while stepHeight < height:
            greyscale = GetGreyAverage(stepWidth, mozeSize, stepHeight, img)
            img = GetGreyPixels(stepWidth, mozeSize, stepHeight, graid, img, greyscale)
            stepHeight += mozeSize
        stepWidth += mozeSize

    return img


def main():
    img_input = input('Что обрабатываем?\n')
    img_output = input('Куда это положим?\n')

    mozeSize = int(input('Какой размер мозайки\n'))
    graidGray = int(input('Какое кол-во градаций\n'))

    img = Image.open(img_input)
    img_arr = np.array(img, dtype=np.uint32)

    width = len(img)
    height = len(img[1])

    gray = 255 / graidGray
    mosaic = GetMosaic(gray, width, height, mozeSize, img_arr)

    res = Image.fromarray(mosaic.astype(np.uint8))
    res.save(img_output)


main()
