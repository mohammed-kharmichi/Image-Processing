import cv2  # type: ignore
import numpy as np # type: ignore


# Erosion pour une image
def erosion(image, element_Struc):
    
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    nbLg_image, nbCol_image = image.shape
    nbLg_elemStruc, nbCol_elemStruc = element_Struc.shape

    centre_elemStruc_x = nbLg_elemStruc // 2
    centre_elemStruc_y = nbCol_elemStruc // 2

    image_erosion = np.zeros((nbLg_image, nbCol_image))

    for i in range(nbLg_image):
        for j in range(nbCol_image):
            min_val = 255  

            for i_elem in range(nbLg_elemStruc):
                for j_elem in range(nbCol_elemStruc):
                    # Calculer les indices correspondants dans l'image
                    i_image = i + i_elem - centre_elemStruc_x
                    j_image = j + j_elem - centre_elemStruc_y
                    
                    if i_image >= 0 and i_image < nbLg_image and j_image >= 0 and j_image < nbCol_image:
                        # Trouver la valeur minimale dans la région couverte par l'élément structurant
                        if element_Struc[i_elem, j_elem] == 1:
                            min_val = min(min_val, image[i_image, j_image])
            
            # Affecter la valeur minimale à l'image érodée
            image_erosion[i, j] = min_val

    return image_erosion


# Dilatation pour une image

def dilatation(image, element_Struct):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    nbLg, nbCol = image.shape
    nbLg_elem, nbCol_elem = element_Struct.shape

    centre_elem_x = nbLg_elem // 2
    centre_elem_y = nbCol_elem // 2

    image_dilate = np.zeros((nbLg, nbCol))

    for i in range(nbLg):
        for j in range(nbCol):
            max_val = 0  # Initialiser la valeur maximale à zéro

            for i_elem in range(nbLg_elem):
                for j_elem in range(nbCol_elem):
                    # Calculer les indices correspondants dans l'image
                    i_image = i + i_elem - centre_elem_x
                    j_image = j + j_elem - centre_elem_y

                    # Vérifier si l'indice est dans les limites de l'image
                    if (i_image >= 0 and i_image < nbLg and
                        j_image >= 0 and j_image < nbCol):
                        # Obtenir la valeur maximale dans la région couverte par l'élément structurant
                        max_val = max(max_val, image[i_image, j_image])

            # Affecter la valeur maximale au pixel de l'image dilatée
            image_dilate[i, j] = max_val

    return image_dilate

# Fonction d'ouverture
def ouverture(image, elementST):
    return dilatation(erosion(image, elementST), elementST)

# Fonction de fermeture
def fermeture(image, elementST):
    return erosion(dilatation(image, elementST), elementST)