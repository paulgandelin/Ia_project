import cv2
import matplotlib.pyplot as plt


def afficher_resultat(image):
    plt.axis('off')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
