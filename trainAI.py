from ultralytics import YOLO

# Charger le modèle pré-entraîné (ex : YOLOv8s)
model = YOLO("runs/detect/train24/weights/last.pt")

# Entraîner le modèle
model.train(
    data="datasets\data.yaml",  # Chemin vers le fichier data.yaml
    epochs=5,         # Nombre d'époques
    batch=16,          # Taille de lot
    imgsz=640          # Taille des images
)
