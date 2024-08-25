# Capture plant health with NDVI and Raspberry Pi

# 순서
1. 라즈베리파이로 사진을 촬영한다.
2. 촬영한 사진은 images폴더에 넣는다.
3. ndvi_constrast.py 까지 진행한다.
4. ndvi_mapping.py를 진행한다

# [Camera Module 3](https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-hello) 
- rpicam-apps을 쉽게 사용할 수 있다. 
```bash
rpicam-hello
```
# [fastiecm.py](./fastiecm.py)  
- 어두운 픽셀을 가져와 흰색으로 만들기
- 원래 픽셀이 밝을 수록 스펙트럼을 따라 색상이 더 멀리 이동합니다. 따라서 어두은 픽셀은 파란색이 되고 밝은 흰색 픽셀은 빨간색으로 변환 합니다. 
# log
- 0824 : raspberry pi camera noir v2를 테스트 완료
- 0825 : 사진은 라즈베리카메라로 촬영하고 이 촬영된 것을 컴퓨터의 opencv로 처리해야함


## Reference 
- [Project Rasberry pi](https://projects.raspberrypi.org/en/projects/astropi-ndvi/0) 
- [What’s that blue thing doing here?](https://www.raspberrypi.com/news/whats-that-blue-thing-doing-here/)
- [Project with web view](https://github.com/benbrackenbury/RPi-NDVI)
- [Plant Hearlth Moniroting System Using Raspberry Pi](https://acadpubl.eu/hub/2018-119-15/4/705.pdf)
- [Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/3)
