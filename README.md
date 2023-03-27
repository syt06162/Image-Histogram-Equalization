# Image-Histogram-Equalization
Image Histogram Equalization "without" using OpenCV2   
OpenCV2 함수를 사용하지 않고 Histogram Equalization 직접 구현.   

## 기능
대비값이 불균형한 이미지 파일 이름을 input으로 넣으면, 대비값이 균일한 이미지 파일을 생성한다.   
![image](https://user-images.githubusercontent.com/92567571/227782995-2ae02b95-3726-41f8-a0ab-9c4b9806bd64.png)

즉 아래와 같이 Histogram Equalization이 진행된 결과가 나온다.
![image](https://user-images.githubusercontent.com/92567571/227783103-03a6a62e-e5d0-45c8-891c-b7a1132d8b23.png)

## 사용 기술
- python 3
- OpenCV2 라이브러리로는 쉽게 구현할 수 있는 기능이지만, 해당 함수를 사용하지 않고 직접 코드로 구현하였다. OpenCV2 함수에 대해서는 code에 주석으로 기재해두었다.

## 사용 방법
- histogram_equalization.py 파일과 같은 경로에 image 파일을 둔다.
- 코드의 1번째 줄에 OPEN_IMAGE_NAME 변수에 해당 image 파일의 파일 이름을 확장자까지 포함해서 작성한다.
- 코드를 실행하면 이미지 결과, 히스토그램 결과 창이 띄워지며, 결과 이미지가 같은 경로에 저장된다.
