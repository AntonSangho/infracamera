import cv2 
import numpy as np

original = cv2.imread('/home/anton/Projects/infracamera/images/park.png') # 이미지 불러오기

def display(image, image_name): 
    image = np.array(image, dtype=float)/float(255) # array로 변환 후 0~1로 정규화 
    shape = image.shape # 이미지 크기 저장
    height = int(shape[0]/2) # 이미지 높이의 절반
    width = int(shape[1]/2) # 이미지 너비의 절반
    image = cv2.resize(image, (width, height)) # 이미지 크기 조절
    cv2.namedWindow(image_name) # 창을 생성 
    cv2.imshow(image_name, image) # 이미지를 창에 띄움
    cv2.waitKey(0) # 키 입력을 기다림
    cv2.destroyAllWindows() # 모든 창을 닫음

def contrast_stretch(im):
    in_min = np.percentile(im, 5) # 최소값
    in_max = np.percentile(im, 95) # 최대값

    out_min = 0 # 출력 최소값
    out_max = 255 # 출력 최대값

    out = im - in_min # 입력 이미지에서 최소값을 뺌
    out *= ((out_min - out_max) / (in_min - in_max)) # 비례식
    out += in_min # 최소값을 더함

    return out

display(original, 'original') # 원본 이미지 출력
contrasted = contrast_stretch(original) # 대비를 높인 이미지 생성
display(contrasted, 'Contrasted original') # 대비를 높인 이미지 출력
cv2.imwrite('contrasted.png', contrasted) # 대비를 높인 이미지 출력 
