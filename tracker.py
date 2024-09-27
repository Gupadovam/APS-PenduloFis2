import cv2
import pandas as pd

# Captura o vídeo
video = cv2.VideoCapture('video.mp4')

# Configura o detector de objetos (subtração de fundo)
object_detector = cv2.createBackgroundSubtractorKNN(history=3000, dist2Threshold=900, detectShadows=False)

data = []
fps = video.get(cv2.CAP_PROP_FPS)
t = 0

while True:
    working, frame = video.read()
    if not working:
        break
    frame = cv2.resize(frame, (600, 600))

    # Aplica o detector de movimento
    mask = object_detector.apply(frame)

    # Encontra contornos na máscara
    countors, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in countors:
        area = cv2.contourArea(cnt)
        if area > 2000:  # Filtra objetos com área maior que 2000, ajustar se necessário
            x, y, w, h = cv2.boundingRect(cnt)
            # Desenha retângulo e exibe coordenadas no frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(frame, f"({int(x + w/2)}, {int(y+h/2)})", (x-15, y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
            # Armazena o tempo e a coordenada x do centro
            data.append({"t": t, "x": (x + w/2)})
            break

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    t += 1.0 / fps  # Incrementa o tempo com base no FPS

    key = cv2.waitKey(30)
    if key == 27:  # Pressiona ESC para sair
        break

video.release()
cv2.destroyAllWindows()

# Exporta os dados para CSV
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
