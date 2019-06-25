import cv2
from matplotlib import pyplot as plt

sample1 = cv2.imread("samples 2/sample1.pgm", 0)
sample2 = cv2.imread("samples 2/sample2.pgm", 0)
sample3 = cv2.imread("samples 2/sample3.pgm", 0)
saturn = cv2.imread("samples 2/saturn.jpg", 0)
hist = cv2.calcHist([sample1], [0], None, [256], [0, 256])

def calc_hist(img):
    hist_array= [0] * 256
    for width in img:
        for value in width:
            hist_array[value] += 1

    return  hist_array

"これはいらない"
def plot_t():
    x = range(0, 256)
    y = calc_hist(sample1)
    plt.plot(x, y)
    plt.fill_between(x, y, 0, facecolor='b', alpha=1)
    plt.show()

def img_to_binary(img, threshold):
    """
    :param img: [][]  imreadで読み込んだ画像
    :param threshold: int 閾値
    :return:
    """
    "img（画像）の中でthreshold（閾値)以上がtrueそれ以外がfalseの２次元配列w作る"
    img_binary = img >= threshold

    plt.imshow(img_binary, cmap='gray')
    plt.show()

def ptile(img, S0, n0 = 0, threshold = 0):
    """
    :param img: [][]    imreadで読み込んだ画像
    :param  S0: (px) * (px) 切り取る面積
    :param  n0: 切り取られない面積
    :param threshold: int 閾値
    :return: none
    """

    "入力画像の面積"
    S = img.size
    "切り取る画像の割合"
    p = S0 / S
    "入力画像のヒストグラムを取得"
    hist_array = calc_hist(img)

    "ヒストグラムのlistの個数回for分を回す"
    for index in range(len(hist_array)):
        "for文が回るたびに切り取られない範囲を足していく"
        n0 += hist_array[index]
        "n0/画像の面積がpを超える場所を閾値とする"
        if n0 / img.size >= p:
            threshold = index
            break

    img_to_binary(img, threshold)



"""
ptile(sample1, 450*400)
ptile(sample2, 240*240)
ptile(sample3, 100*100)
"""
ptile(saturn, 200*200)