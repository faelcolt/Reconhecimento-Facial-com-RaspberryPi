import cv2

# Carrega o classificador de rostos
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Abre a câmera padrão (ou outra especificada) e captura imagens
cap = cv2.VideoCapture(0)

# Loop para capturar e processar imagens em tempo real
while True:
    ret, frame = cap.read() # Captura uma imagem da câmera

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos na imagem em escala de cinza
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Desenha um retângulo ao redor do rosto detectado na imagem original
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Exibe a imagem com as faces detectadas em uma janela
    cv2.imshow('frame',frame)

    # Interrompe o loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos da câmera e fecha a janela
cap.release()
cv2.destroyAllWindows()
