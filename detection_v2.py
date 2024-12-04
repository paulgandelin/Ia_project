import cv2
import time
from ultralytics import YOLO
from appel_urgence_v1 import envoi_mail
#importing Yolo model
model = YOLO("runs/detect/train24/weights/last.pt")

#importing video stream
video= cv2.VideoCapture(0)


#loop code
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    results = model.predict(source=frame, conf=0.5) #  source = images en cours de vision conf = confiance 
    annotated_frame = results[0].plot() # annote les images 

    for r in results[0].boxes:
        if r.cls == 0 or r.cls == 1:  # attention valeur pour le feu à changer global
            print("fire detected !")
            #envoi_mail(f=1)
            #time.sleep(5)
            break
        else :
            break
    
    cv2.imshow("fire dection aps", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#close all and free the memory
video.release()
cv2.destroyAllWindows()




