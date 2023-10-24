import cv2
import numpy as np

# Conectar a la cámara. El argumento '0' indica la cámara número 0.
cap = cv2.VideoCapture(0)
image = cv2.imread("gatitoSorpresa.png")

while (True):
    # Capturar una imagen de la cámara
    ret, frame = cap.read()
    # Reducir a la mitad el tamaño si es grande
    h, w, _ = frame.shape[:3]
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image,(640, 480))

    # Convertir el espacio de color utilizando cvtColor. El segundo argumento especifica la conversión de BGR a HSV.
    # En procesamiento de imágenes, también se usa a menudo BGR a escala de grises (Gray). En ese caso, se especifica cv2.COLOR_BGR2GRAY.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Preparar para especificar los valores de H, S y V a extraer.
    # En este caso, H está en el rango de 40 a 90, S está en el rango de 20 a 255 y V está en el rango de 20 a 255. (Cambios 1 de 2)
    lower = np.array([45, 25, 25])
    upper = np.array([90, 255, 255])

    # Crear una imagen con píxeles blancos donde el color cae dentro del rango especificado y negros en otros lugares.
    mask = cv2.inRange(hsv, lower, upper)
    
    # Dado que el proceso anterior extrae el verde, invertimos la imagen a blanco y negro (Cambios 2 de 2)
    

    # Extraer colores de la imagen original basándonos en la máscara en blanco y negro.
    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    f = np.where(f==0, image, f)

    # Mostrar las imágenes en ventanas separadas.
    cv2.imshow("Cámara", frame)
    cv2.imshow("Máscara", mask)
    cv2.imshow("Resultado", f)

    # Esperar 30 milisegundos para una entrada de tecla.
    key = cv2.waitKey(30) & 0xFF

    # Si se presiona 'q', salir del bucle.

    if key == ord('1'):
        image = cv2.imread("beach.jpg")

    elif key == ord('2'):
        image = cv2.imread("vaporwave.jpg")

    elif key == ord('3'):
        image = cv2.imread("macaco.jpg")
    
    elif key == ord('4'):
        image = cv2.imread("furby.jpg")
    
    elif key == ord('0'):
        image = cv2.imread("gatitoSorpresa.png")

    elif key == ord('q'):
        break

# Liberar la captura.
cap.release()
cv2.waitKey(1)

# Cerrar todas las ventanas.
cv2.destroyAllWindows()

# Agregar una breve espera como precaución antes de salir.
cv2.waitKey(1)