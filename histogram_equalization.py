OPEN_IMAGE_NAME = "sample_image.jpg"

# cv2를 이용하지 않고 직접 구현하는 것이 목표이지만,
# 이미지 및 히스토그램 시각화에서만 라이브러리 이용
import cv2

import matplotlib.pyplot as plt
import copy
import numpy as np

# 사진 가져오기
original_img = cv2.imread(OPEN_IMAGE_NAME, cv2.IMREAD_GRAYSCALE)



### ----- 이퀄라이제이션 전 -----

# original 히스토그램 생성 및 계산
# cv2.calcHist() 함수로 대체 가능하나, 직접 구현해본다.

L = 256 # 우리 이미지는 0 - 255 사이의 밝기 값을 가지므로, L = 256 이다.

def makeHistogram(img):
    hist = [0 for i in range(0, L)] # 0 - 255 
    # original 히스토그램 계산
    for row in img:
        for value in row:
            hist[value] += 1
    return hist

original_hist = makeHistogram(original_img)



### ----- 이퀄라이제이션 과정 -----

# cv2.equalizeHist() 함수로 대체 가능하나, 직접 구현해본다.

# 누적합 알고리즘으로 cdf 생성
original_cdf = []
sum = 0
for value in original_hist:
    sum += value
    original_cdf.append(sum)
    
# 이퀄라이제이션을 하는 맵(함수) 구현.
# 이 함수는 추후 이미지 이퀄라이저에 직접 사용됨
# 예를 들어 밝기값(1)이 밝기값(3)으로 이퀄라이제이션이 되어야 한다면,
# equalizizer_map[1] 의 값은 3이 될 것임. 이를 뒤에서 이용해 이퀄라이제이션 진행
equalizizer_map = []
for i in range(0,L):
    eq_val = round(original_cdf[i] * (L-1) / sum)
    equalizizer_map.append(eq_val)

# 이를 이용해 기존 image 이퀄라이제이션 진행
equalize_img = copy.deepcopy(original_img)
for row in range(len(equalize_img)):
    for column in range(len(equalize_img[row])):
        origin_val = original_img[row][column]
        equalize_val = equalizizer_map[origin_val]
        equalize_img[row][column] = equalize_val

# 이퀄라이제이션 된 히스토그램도 계산
equalize_hist = makeHistogram(equalize_img)



### ----- equalize 이미지 저장 -----
NEW_FILE_NAME = OPEN_IMAGE_NAME.split(".")
cv2.imwrite(NEW_FILE_NAME[0] + "_equalized" + "." + NEW_FILE_NAME[1] ,equalize_img)
    

    
### ----- 시각화 과정 -----
# 이미지 시각화
img_stack = np.hstack((original_img, equalize_img))
cv2.imshow("original , equalize", img_stack)

# 히스토그램 시각화
plt.figure(figsize=(12,6))
plt.subplot(121)
plt.bar([i for i in range(0,L)], original_hist) # 막대그래프
plt.subplot(122)
plt.bar([i for i in range(0,L)], equalize_hist)
plt.show()