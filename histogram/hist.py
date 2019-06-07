import cv2
from matplotlib import pyplot as plt

sample1 = cv2.imread("samples 2/sample1.pgm", 0)
sample2 = cv2.imread("samples 2/sample2.pgm", 0)
sample3 = cv2.imread("samples 2/sample3.pgm", 0)
hist = cv2.calcHist([sample1], [0], None, [256], [0, 256])


# plt.hist(img.ravel(),256,[0,256])


def calc_hist(img):
    hist_1num = [0] * 256
    for a in img:
        for b in a:
            hist_1num[b] += 1

    return  hist_1num

x = range(0, 256)
y = calc_hist(sample1)
plt.plot(x, y)
plt.fill_between(x, y, 0, facecolor='b', alpha=1)
plt.show()
