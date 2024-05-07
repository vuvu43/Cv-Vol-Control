from classHandDetec import hand_detector
import cv2 as cv
import time


def main():
    ptime, ctime = 0, 0 #parametros para calcular o fps do vídeo
    cap = cv.VideoCapture(0) #captura de vídeo ao vivo da webcam
    detector = hand_detector() #instancia a classe para detectar as mãos
    fps=True #True se quiser saber fps do vídeo, False caso contrário

    while True:
        sucesso, img = cap.read() #lê da webcam
        img = detector.find_hands(img, draw=True) #detecta a mão e desenha os landmarks
        lmList = detector.find_position(img, draw_lms=[0, 4, 8, 12, 16, 20]) #detecta landmarks e desenha se desejado

        img = cv.flip(img, 1) #inverte a imagem 
        if fps:
            #calcula o fps
            ctime = time.time()
            fps = 1/(ctime - ptime)
            ptime = ctime
            #display do fps no vídeo
            cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 2) 
        
        cv.imshow("Webcam", img)
        cv.waitKey(1)
    
    return



if __name__ == "__main__":
    main()