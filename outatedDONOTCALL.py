import cv2
import numpy as np

def detect_smoke(image_path):
    # Lire l'image
    img = cv2.imread(image_path)
    
    # Vérifier si l'image est chargée correctement
    if img is None:
        print(f"Erreur : Impossible de charger l'image à l'emplacement : {image_path}")
        return False
    
    print("Image chargée avec succès.")

    # Convertir l'image en espace de couleur HSV (Teinte, Saturation, Valeur)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Ajuster la plage pour la fumée
    lower_gray = np.array([0, 0, 100])    
    upper_gray = np.array([180, 50, 255]) 
    
    # Créer un masque pour détecter les zones qui correspondent à la plage de gris (fumée)
    smoke_mask = cv2.inRange(hsv_img, lower_gray, upper_gray)
    
    print("Masque de fumée créé.")

    # Appliquer un flou pour réduire le bruit
    smoke_mask = cv2.GaussianBlur(smoke_mask, (15, 15), 0)

    # Appliquer Canny Edge Detection
    edges = cv2.Canny(smoke_mask, 50, 150)
    
    print("Détection des bords appliquée.")

    # Trouver les contours des zones de fumée
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    print(f"Contours détectés : {len(contours)}")

    # Dessiner des rectangles autour des zones détectées comme de la fumée
    for contour in contours:
        # Ignorer les petits contours
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Afficher l'image originale avec les zones suspectes encadrées
    cv2.imshow('Détection de fumée améliorée', img)
    
    # Attendre la pression d'une touche pour fermer la fenêtre
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Calculer le pourcentage de zones suspectes
    smoke_area = np.sum(smoke_mask > 0)
    total_area = img.shape[0] * img.shape[1]
    smoke_percentage = (smoke_area / total_area) * 100
    
    print(f"Pourcentage de zones potentiellement fumées : {smoke_percentage:.2f}%")
    
    # Seuil de détection
    if smoke_percentage > 10:
        print("Fumée détectée dans l'image.")
        return True
    else:
        print("Pas de fumée détectée dans l'image.")
        return False


# Exemple d'utilisation :
image_path = 'C:\\Users\\octav\\OneDrive\\Documents\\ECE\\robotique\\imagesfumees.jpg'
detect_smoke(image_path)
