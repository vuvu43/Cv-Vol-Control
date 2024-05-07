import cv2 as cv
import mediapipe as mp

class hand_detector():
    def __init__(self, mode=False, maxHands=2, modelComplexity=1,detectionCon=0.5, trackCon=0.5):
        self.mode = mode #True se for imagem estática
        self.maxHands = maxHands #Quantidade máxima de mãos detectadas
        self.detectionCon = detectionCon #Threshold de confiança
        self.trackCon = trackCon #Threshold de confiança
        self.modelComplexity = modelComplexity

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, 
                                        self.maxHands, 
                                        self.modelComplexity, 
                                        self.detectionCon, 
                                        self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB) #converte os canais de cor para RGB
        result = self.hands.process(imgRGB) #faz tracking da mão

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        
        return img
