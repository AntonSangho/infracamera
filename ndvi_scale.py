import cv2 
import numpy as np

image = cv2.imread('/home/anton/Projects/infracamera/images/park.png') # 이미지 불러오기
image = np.array(image, dtype=float)/float(255) # array로 변환 후 0~1로 정규화 
shape = image.shape # 이미지 크기 저장
height = int(shape[0]/2) # 이미지 높이의 절반
width = int(shape[1]/2) # 이미지 너비의 절반
image = cv2.resize(image, (width, height)) # 이미지 크기 조절
cv2.namedWindow('Original') # 창을 생성 
cv2.imshow('Original', image) # 이미지를 창에 띄움
cv2.waitKey(0) # 키 입력을 기다림
cv2.destroyAllWindows() # 모든 창을 닫음
