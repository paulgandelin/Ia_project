def CreerTab_donnee(chemin_image):
    with open(chemin_image, "rb") as f:
        byte_array = bytearray(f.read())

    image_array = np.asarray(byte_array, dtype="uint8")
    return image_array



