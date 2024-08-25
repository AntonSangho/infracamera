import cv2 
import numpy as np

image = cv2.imread('/home/anton/Projects/infracamera/images/park.png') # 이미지 불러오기
image = np.array(image, dtype=float)/float(255) # array로 변환 후 0~1로 정규화 
cv2.namedWindow('Original') # 창을 생성 
cv2.imshow('Original', image) # 이미지를 창에 띄움
cv2.waitKey(0) # 키 입력을 기다림
cv2.destroyAllWindows() # 모든 창을 닫음
