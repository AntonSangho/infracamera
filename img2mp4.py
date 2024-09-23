import cv2
import os

def create_video_from_images(image_folder, output_video, frame_rate=30):
    # 이미지 파일들을 읽어오기 위해 파일 리스트 정렬
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images.sort()

    # 첫 번째 이미지를 읽어와서 영상의 크기를 설정
    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = first_image.shape

    # 동영상 코덱 설정 및 비디오 작성자 초기화
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4 코덱 설정
    video = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

    # 모든 이미지 파일을 비디오에 추가
    for image in images:
        img = cv2.imread(os.path.join(image_folder, image))
        video.write(img)

    # 비디오 작성 완료 후 릴리즈
    video.release()

# 예시 사용법
image_folder = './images'  # 이미지 파일이 있는 폴더 경로
output_video = 'output_video.mp4'  # 생성할 비디오 파일명
create_video_from_images(image_folder, output_video)

