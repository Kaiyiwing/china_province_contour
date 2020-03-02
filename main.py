import cv2
import numpy as np
import os

# 羽化轮廓, 目的解决 shapewordle 对部分图片的不兼容

def simplify_contour(img_dir):
    img = cv2.imread(img_dir)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)  # 转换为二值图像
    _, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 提取轮廓
    # 简化边缘
    approxs = []
    for i in contours:
        # 第二个参数越大简化程度越高
        approx = cv2.approxPolyDP(i, 8, True)
        approxs.append(approx)
    # 创建新的图片
    img2 = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    # 使用白色填充图片区域,默认为黑色
    img2.fill(255)
    cv2.drawContours(img2, approxs, -1, (0, 0, 0), thickness=-1)

    img_dir = img_dir.split('/')[1].split('.')
    output_dir = 'provinces_s/'+img_dir[0] + '.'+img_dir[1]
    cv2.imwrite(output_dir, img2)
path = 'provinces'
files = os.listdir(path)
for file in files:
    if file.split('.')[1] == 'png':
        simplify_contour(path+'/'+file)
