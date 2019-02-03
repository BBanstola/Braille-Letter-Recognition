from __future__ import division
import PIL
from os.path import join, dirname, realpath
from scipy.misc import imread
import numpy as np
import os, glob
import dill
from PIL import Image



UPLOAD_FOLDER1 = join(dirname(realpath(__file__)),'templates/mulsegimages/')
UPLOAD_FOLDER2 = join(dirname(realpath(__file__)),'templates/traindata/')
UPLOAD_FOLDER3 = join(dirname(realpath(__file__)),'templates/temp')

def identify():

    net='nn.dill'
    filename ='median_blurred.png'

    with open((UPLOAD_FOLDER2)+net, 'rb') as f:  # load the trained Neural Network
        nn = dill.load(f)

    char_number_map = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
                       12: 'm', 13: 'n', 14: 'o',
                       15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y',
                       25: 'z', 26: '!', 27: '"', 28: ',',
                       29: '-', 30: '.', 31: '?'}

    im = Image.open((UPLOAD_FOLDER1)+filename)
    im = im.convert("P")
    im2 = Image.new("P", im.size, 255)



    temp = {}
    for x in range(im.size[1]):  # convert the image to grayscale
        for y in range(im.size[0]):
            pix = im.getpixel((y, x))
            temp[pix] = pix
            if pix <= 52:
                im2.putpixel((y, x), 0)

    im2.save((UPLOAD_FOLDER3)+ filename.split(".")[0] + ".gif")

    image = im2.resize((30, 42), PIL.Image.LANCZOS)

    image.save((UPLOAD_FOLDER1)+'out.bmp')

    imag = imread((UPLOAD_FOLDER1)+'out.bmp')

    value = imag.flatten()

    value = 255 - value
    inputs = (np.asfarray(value) // 255 * 0.99) + 0.01
    output = np.argmax(nn.predict(inputs))

    x=(char_number_map[output])


    filelist = glob.glob((UPLOAD_FOLDER3)+"*.gif")
    for f in filelist:
        os.remove(f)

    return x

