from classHandDetec import hand_detector
import cv2 as cv
import numpy as np
import time
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def main():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume) #vars para controlar volume
    ptime, ctime = 0, 0 #parametros para calcular o fps do vídeo
    cap = cv.VideoCapture(0) #captura de vídeo ao vivo da webcam
    cap.set(3, 640) #tamanho da janela no eixo x
    cap.set(4, 480) #tamanho da janela no eixo y
    detector = hand_detector(detectionCon=0.7) #instancia a classe para detectar as mãos
    fps = True #True se quiser saber fps do vídeo, False caso contrário

    while True:
        sucesso, img = cap.read() #lê da webcam
        img = detector.find_hands(img, draw=True) #detecta a mão e desenha os landmarks
        lmList = detector.find_position(img, draw_lms=[4, 8]) #detecta landmarks e desenha se desejado

        if lmList: #se houverem landmarks...
            dedaox, dedaoy = lmList[4][1], lmList[4][2] #ponta do dedão
            indx, indy = lmList[8][1], lmList[8][2] #ponta do indicador
            cx, cy = (dedaox+indx)//2, (dedaoy+indy)//2 #ponto médio entre os 2
            
            cv.line(img, (dedaox, dedaoy), (indx, indy), (255,10,10), 3)
            cv.circle(img, (cx, cy), 7, (0,255,0), cv.FILLED)

            dist = math.hypot(dedaox-indx, dedaoy-indy) #distância entre a ponta dos dedos
            if dist < 15: #se a distância entre os dedos for a menor, mude a cor do "botão"
                cv.circle(img, (cx, cy), 7, (10,10,255), cv.Filled)

            #15 - 125 é o que eu setei como distâncias mínima e máxima entres os dedos
            #-65.25 - 0 é o range do volume no sistema
            #função para converter a distância para o range do volume do sistema
            vol = np.interp(dist, [15, 125], [-65.25, 0]) 
            volume.SetMasterVolumeLevel(vol, None)
            

        img = cv.flip(img, 1) #inverte a imagem 
        if fps:
            #calcula o fps
            ctime = time.time()
            fps = 1/(ctime - ptime)
            ptime = ctime
            #display do fps no vídeo
            cv.putText(img,"FPS: " + str(int(fps)), (20, 60), cv.FONT_HERSHEY_PLAIN, 3, (255,20,10), 2) 
        
        cv.imshow("Webcam", img)
        cv.waitKey(1)



if __name__ == "__main__":
    main()