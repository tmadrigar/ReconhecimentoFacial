import cv2
import time

USAR_ARDUINO = True

if USAR_ARDUINO:
    import serial
    arduino = serial.Serial('COM7', 9600)
    time.sleep(2)

def detectar_direcao(faces, largura_frame):
    if len(faces) == 0:
        return "CENTRO"

    # Seleciona o rosto com maior área (largura * altura)
    rosto_maior = max(faces, key=lambda f: f[2] * f[3])
    x, y, w, h = rosto_maior
    centro = x + w // 2

    if centro < 280:
        return "ESQUERDA"
    elif centro > 360:
        return "DIREITA"
    return "CENTRO"


def main():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Corrige a imagem espelhada
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=6, minSize=(60, 60))

        direcao = detectar_direcao(faces, frame.shape[1])

        if USAR_ARDUINO:
            if direcao == 'ESQUERDA':
                arduino.write(b'E')
            elif direcao == 'DIREITA':
                arduino.write(b'D')
            elif direcao == 'CENTRO':
                arduino.write(b'C')

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Usa setas ASCII para compatibilidade com OpenCV
        if direcao == "ESQUERDA":
            texto = "<-- ESQUERDA"
        elif direcao == "DIREITA":
            texto = "DIREITA -->"
        else:
            texto = "|| CENTRALIZADO ||"

        cv2.putText(frame, texto, (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (0, 255, 0), 3)

        cv2.imshow('Detecção Facial com Direção', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
