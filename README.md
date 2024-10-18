# Capture plant health with NDVI and Raspberry Pi

# 하드웨어 
- 라즈베리파이 4 
- 라즈베리파이 카메라 모듈 2 NoIR
- 라즈베리파이용 파워아답터

# 개발환경 
- 라즈베리파이 OS: 64-bit Bookworm with the Raspberry Pi Desktop

# Headless 모드로 라즈베리파이 설정

1. ssh 설정
```bash
sudo raspi-config
```
2. Advanced Options -> SSH -> Enable

3. [raspbserry pi connect로 원격 접속](https://connect.raspberrypi.com/devices) 

# [사진 촬영](https://www.raspberrypi.com/documentation/computers/camera_software.html#via-cron) 
1. timelapse.sh 만들기 
```bash
#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M")
rpicam-still -o /home/<username>/infracamera/images/$DATE.jpg
```
2. timelase.sh 의 권한 변경
```bash
chomd +x timelase.sh
```
3. crontab -e 로 30분 단위로 timelaps.sh 실행하도록 정하기 
```bash
*/30 * * * * /home/<username>/infracamera/timelapse.sh 2>&1
```

# [WiFi 설정](https://youtu.be/QjSn33jbzFM?feature=shared)
1. nmcli의 ui버전인 nmtui 실행
```bash
nmtui
```
2. Edit a connection
3. Add
4. SSID 입력
5. Security를 WPA & WPA2 Personal로 변경
6. Password 입력






# 후처리순서
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

# 원격 파일시스템 - filebrowser

## 설 치 및 자동실행
1. filebrowser 설치 
```bash
curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash
```
2. filerbrowser를 같은 네트워크에서 접속가능하도록 실행
```bash
filebrowser 0.0.0.0 -a 
```
3. 로그인하기 
- localhost:8080으로 접속
- ID : admin PW : admin

4. filebrowser를 pm2로 자동실행하기하기
- pm2 설치
```bash
sudo apt update
sudo apt install -y nodejs npm
sudo npm install pm2@latest -g
```
- filebrowser 경로 확인
```bash
which filebrowser
```
- pm2로 filebrowser 실행
```bash
pm2 start filebrowser --name "filebrowser" -- -r /home/[pi] -a 0.0.0.0 --port 8080
```
- pm2가 자동으로 실행되도록 systemd에 등록
```bash
sudo env PATH=$PATH:/usr/local/bin pm2 startup systemd -u [pi] --hp /home/[pi]
```
- pm2로 실행한 프로세스를 저장
```bash
pm2 save
```
## 사용자 관리 
1. admin 계정으로 로그인
2. 홈에서 users 폴더 만들기
3. users 폴더에서 사용자 아이디 추가 예)pi1,pi2,pi3,....
2. 설정 -> 전역설정 -> Auto create user home dir while adding new user 체크 
3. 설정 -> 사용자관리 -> 신규
4. 사용자 추가
5. 사용자 이름 : ex) pi1
6. 범위 : ex) /users/pi1
7. 권한 해제
- 파일이나 디렉토리 생성하기
- 파일이나 디렉토리 삭제하기
- 파일 편집
- 파일 이름 변경 또는 디렉토리 이동 









# log
- 0824 : raspberry pi camera noir v2를 테스트 완료
- 0825 : 사진은 라즈베리카메라로 촬영하고 이 촬영된 것을 컴퓨터의 opencv로 처리해야함


## Reference 
- [Project Rasberry pi](https://projects.raspberrypi.org/en/projects/astropi-ndvi/0) 
- [What’s that blue thing doing here?](https://www.raspberrypi.com/news/whats-that-blue-thing-doing-here/)
- [Project with web view](https://github.com/benbrackenbury/RPi-NDVI)
- [Plant Hearlth Moniroting System Using Raspberry Pi](https://acadpubl.eu/hub/2018-119-15/4/705.pdf)
- [Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/3)
