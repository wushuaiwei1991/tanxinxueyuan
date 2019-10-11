import matplotlib.pyplot as plt

# 读取图片的数据，存放到img
img = plt.imread('E:\网盘照片\图片\MX4手机相册\P41026-150818-001.jpg')
print(img.shape)  # 打印图片的大小

plt.imshow(img)   # 展示图片