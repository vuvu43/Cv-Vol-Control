# Modo de uso:
Só funciona em windows.
```console
cd Volume-Controler
python main.py
```

# Como funciona

Utilizando as bibliotecas opencv e mediapipe, a imagem da câmera é capturada. Depois disso é calculado a distância entre o seu dedão e o indicador. Baseado nessa distância, o volume do seu computador será setado no range de 0 - 100, quanto mais pertos menor o volume, quanto mais distantes maior o volume.\br

Recomendo abrir o controle de volume do computador para ver ele mexer junto com sua mão.
