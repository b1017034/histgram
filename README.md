# histgram
画像解析の課題

```
"""
ptile(sample1, 450*400)
ptile(sample2, 240*240)
ptile(sample3, 100*100)
"""
```

コメントアウトは適宜外して
450*400とかの数字は適当なので試行錯誤して決めてください(単位はpx)

画像を読み込む際は下記のように
samples 2フォルダの中に画像を入れて
saturn = cv2.imread("samples 2/saturn", 0)
のようにすれば読み込める

