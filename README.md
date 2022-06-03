# NoktalardanNesneyiAlgilama

### Özellikler

- Dahili Klasördeki Resim Dosyasını alır.
- Ekranda nokta (fare tık ile ) oluşturur.
- Oluşturulan noktalardan yeni frame oluşturur.



### Sonuç 
Altta uygulamanın çalışır hali gif ile verilmiştir.  



![](/app-run.gif)

>Sonuç Proje Gif

### Ön kurulum

`pip install numpy`

`pip install opencv-python`
### Kodlar ve Anlatım :

### Kullanacağımız kütüphanelerimizi import edelim
    import cv2
    import numpy as np
### 
### Çerçeve olusturmak icin numpy'dan faydalanalım - 4 nokta ve 2 eksen (x , y )
    frame = np.zeros((4, 2), np.int)
    tiklamaSayaci = 0
### 
### Fare tıklaması için fonksiyon oluşturalım oluşturalım
    def fareTiklama(event, x, y, flags, params):
      global tiklamaSayaci
      if event == cv2.EVENT_LBUTTONDOWN:
        frame[tiklamaSayaci] = x, y
        tiklamaSayaci += 1
        print(frame)
### 
### Orjinal görüntümüzü okuyalım
    img = cv2.imread("images/clean_code_book.jpg")
### 
#### Döngü oluşturalım, tıklama (nokta) sayısı 4'e (dikdörtgen) ulaşırsa görüntüyü çarpıtalım ardından ekrana basalım.

    while True:
      if tiklamaSayaci == 4:
        width, height = 250, 350
        pts1 = np.float32([frame[0], frame[1], frame[2], frame[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("", imgOutput)
        cv2.waitKey(0)
      for x in range(0, 4):
        cv2.circle(img, (frame[x][0], frame[x][1]), 5, (0, 0, 255), cv2.FILLED)    

#### Fare işaretçisi için setMouseCallback methodunu kullanalım
    cv2.imshow("", img)
    cv2.setMouseCallback("", fareTiklama)
    cv2.waitKey(1)
    
### KAYNAKLAR :

https://docs.opencv.org/4.x/

https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/

https://numpy.org/doc/stable/reference/generated/numpy.zeros.html?highlight=zeros

https://www.computervision.zone/topic/chapter-5-warp-perspective-2/
    

     

### Teşekkürler
