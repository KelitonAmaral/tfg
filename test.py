import cv2

# print("hello world")

# tracker = cv

#Cria um objeto rastreador de nome 'tracker', que usa o algoritmo KCF
tracker = cv2.TrackerKCF_create()


# Variável 'video' que vai receber o video com o objeto a ser rastreado
video = cv2.VideoCapture('videos/hang-power-clean.mp4')

# read() dessa forma, sem argumentos, vai pegar o primeiro frame do vídeo
# e atribuir à variável 'frame'
ok, frame = video.read()

# 'bbox é a variável que guarda o bounding box, isto é, a 'caixa' que marca a região de interesse
# (Region of Interest ou ROI)'
# a função selectROI recebe o 'frame' que contém o objeto que queremos rastrear
# ao ler essa frase, o programa vai abrir uma segunda janela com apenas o primeiro frame do video
# agora, o usuário deve usar o mouse, clicando e segurando o botão esquerdo e arrastando
# até criar uma 'caixa' que contém o objeto que se pretende rastrear
# quando terminar a seleção, tecle ENTER para confirmar ou ESC para cancelar
bbox = cv2.selectROI(frame)

# O print a seguir mostra valores discretos (x, y, w, h), onde x e y são as coordenadas
# do ponto inicial do bounding box e w e h são respectivamente a largura e a altura 
# do bounding box
print(bbox)



# print(ok)
