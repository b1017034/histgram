import cv2
from matplotlib import pyplot as plt
import numpy as np


sample1 = cv2.imread("samples 2/sample1.pgm", 0)
sample2 = cv2.imread("samples 2/sample2.pgm", 0)
sample3 = cv2.imread("samples 2/sample3.pgm", 0)
hist = cv2.calcHist([sample1], [0], None, [256], [0, 256])


# plt.hist(img.ravel(),256,[0,256])


def calc_hist(img):
    hist_array= [0] * 256
    for width in img:
        for value in width:
            hist_array[value] += 1

    return  hist_array

def plot_t():
    x = range(0, 256)
    y = calc_hist(sample1)
    plt.plot(x, y)
    plt.fill_between(x, y, 0, facecolor='b', alpha=1)
    plt.show()

def img_to_binary(img, threshold):
    img_binary = img >= threshold

    plt.imshow(img_binary, cmap='gray')
    plt.show()

def ptile(img, S0):
    """
    :param img: [][]
    :param  S0: (px) * (px)
    :return: none
    """
    n0 = 0
    threshold = 0

    S = img.size
    p = S0 / S
    print(p)
    hist_array = calc_hist(img)

    for index in range(len(hist_array)):
        n0 += hist_array[index]
        if n0 / img.size >= p:
            print(index)
            threshold = index
            break

    img_to_binary(img, threshold)



"ptile(sample1, 100 * 100)"
ptile(sample1, 450*400)