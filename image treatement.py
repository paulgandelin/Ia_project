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
        
def PassageGris(image):
    res=cv2.resize(image, dsize=(40,40), interpolation=cv2.INTER_CUBIC)
    print(res.shape)
    res=cv2.cvtColor(res,cv2.COLOR_RGB2GRAY)# to 3D to 1D
    print(res.shape)
    return res

def PassageBinaire_AfficheResultat(res):
    res=cv2.threshold(res,127,255,cv2.THRESH_BINARY)[1]
    d=res
    for row in range (0,40):
        for col in range(0,40):
            print('%03d' %d[row][col],end=' ')
        print('')

    afficher_resultat(image=res)
    return d

def Kernel_analyse(image_bw):
    kernel=np.matrix([[-10,0,10],[-10,0,10],[-10,0,10]]) #[0,0,0],[0,1,0],[0,0,0] image pas changé 
    print(kernel)
    image1=cv2.filter2D(image_bw,-1, kernel)
    afficher_resultat(image=image1)
    return image1
def convert_to_bw(image_array):
    image_bw=cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
    (thresh, image_bw)= cv2.threshold(image_bw,127,255,cv2.THRESH_BINARY)
    afficher_resultat(image=image_bw)
    return image_bw
