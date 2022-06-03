# kütüphanelerimizi import edelim
import cv2
import numpy as np

# cerceve olusturmak icin - 4 nokta ve 2 eksen (x , y )
frame = np.zeros((4, 2), np.int)
tiklamaSayaci = 0

def fareTiklama(event, x, y, flags, params):
    global tiklamaSayaci
    if event == cv2.EVENT_LBUTTONDOWN:
        frame[tiklamaSayaci] = x, y
        tiklamaSayaci += 1
        print(frame)

img = cv2.imread("images/clean_code_book.jpg")

# dongude goruntuyu carpıtalım
while True:

    # tıklama (nokta ) 4 'e ulastıgında
    # kaynak : https://www.computervision.zone/topic/chapter-5-warp-perspective-2/
    if tiklamaSayaci == 4:
        width, height = 250, 350
        # frame ' e göre nokta değerlerini otomatik almak için
        pts1 = np.float32([frame[0], frame[1], frame[2], frame[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        # yeni resmi ekrana basalım
        cv2.imshow("", imgOutput)
        cv2.waitKey(0)

    # nokta (daire ) için openCv circle() metodunu kullanırız
    for x in range(0, 4):
        # kaynak : https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/
        cv2.circle(img, (frame[x][0], frame[x][1]), 5, (0, 0, 255), cv2.FILLED)

    cv2.imshow("", img)
    cv2.setMouseCallback("", fareTiklama)
    cv2.waitKey(1)
