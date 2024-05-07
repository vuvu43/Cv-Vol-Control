from classHandDetec import hand_detector
import cv2 as cv
import time


def main():
    ptime, ctime = 0, 0 #parametros para calcular o fps do vídeo
    cap = cv.VideoCapture(0) #captura de vídeo ao vivo da webcam
    detector = hand_detector() #instancia a classe para detectar as mãos

    while True:
        sucesso, img = cap.read()
        img = detector.find_hands(img)

        ctime = time.time()
        fps = 1/(ctime - ptime)
        ptime = ctime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 2)
        cv.imshow("Video - Ao Vivo", cv.flip(img, 1))
        cv.waitKey(1)
    
    return



if __name__ == "__main__":
    main()