import cv2
import time
from ultralytics import YOLO
from appel_urgence_v1 import envoi_mail
#importing Yolo model
model = YOLO("runs/detect/train24/weights/last.pt")

#importing video stream
video= cv2.VideoCapture(0)








