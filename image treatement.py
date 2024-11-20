def CreerTab_donnee(chemin_image):
    with open(chemin_image, "rb") as f:
        byte_array = bytearray(f.read())

    image_array = np.asarray(byte_array, dtype="uint8")
    return image_array


def Afficher_image(image_array):
    print(f'shape of image {image_array.shape}')
    image_afficher= cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    if image_afficher is None:
        print("Erreur : Impossible de décoder l'image")
    else:
        afficher_resultat(image=image_afficher)
        return image_afficher


