import cv2  # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt  # type: ignore

# Lire une image
def read_image(image_path):
    image = cv2.imread(image_path)
    return image



# Image inverse
def negative_image(image):
    if len(image.shape) == 2:  # Niveaux de gris
        # Calculer l'image négative
        negative_image = 255 - image
    elif len(image.shape) == 3:  # Couleur
        # Calculer l'image négative pour chaque canal de couleur
        negative_image = cv2.subtract(255, image)
    
    return negative_image


# Retationner une image
def rotate_image(image, angle):
    # Convertir l'angle en radians
    angle_rad = np.radians(angle)

    # Obtenir les dimensions de l'image
    height, width = image.shape[:2]

    # Calculer le centre de l'image
    center_x = width // 2
    center_y = height // 2

    # Créer une nouvelle image pour stocker l'image tournée
    rotated_image = np.zeros_like(image)

    # Boucler à travers chaque pixel de l'image originale
    for y in range(height):
        for x in range(width):
            # Coordonnées du pixel d'origine centré sur l'origine
            x_centered = x - center_x
            y_centered = y - center_y

            # Appliquer la rotation à ces coordonnées
            x_rotated = int(x_centered * np.cos(angle_rad) - y_centered * np.sin(angle_rad) + center_x)
            y_rotated = int(x_centered * np.sin(angle_rad) + y_centered * np.cos(angle_rad) + center_y)

            # Assurer que les nouvelles coordonnées se trouvent dans les limites de l'image
            if 0 <= x_rotated < width and 0 <= y_rotated < height:
                rotated_image[y, x] = image[y_rotated, x_rotated]

    return rotated_image


# Redimensionner une image
def resize_image(image, nouvelle_taille=None, pourcentage_redimensionnement=None):
    if nouvelle_taille is not None:
        image_redimensionnee = cv2.resize(image, nouvelle_taille, interpolation=cv2.INTER_AREA)
    elif pourcentage_redimensionnement is not None:
        nouvelle_largeur = int(image.shape[1] * pourcentage_redimensionnement / 100)
        nouvelle_hauteur = int(image.shape[0] * pourcentage_redimensionnement / 100)
        nouvelle_taille = (nouvelle_largeur, nouvelle_hauteur)
        image_redimensionnee = cv2.resize(image, nouvelle_taille)
    
    return image_redimensionnee


# Calculer l'histogramme d'une seule canal
def oneCanalHist(image):
    # Initialiser un histogramme vide
    hist = np.zeros(256)

    # Compter l'occurrence de chaque intensité de pixel dans l'image
    height, width = image.shape
    for y in range(height):
        for x in range(width):
            intensity = image[y, x]
            hist[intensity] += 1

    return hist

# Calcule de l'histogramme soit image en niveaux de gris ou couleur
def calculer_histogramme(image):
    if len(image.shape) == 2:
        hist = oneCanalHist(image)
        return hist, None, None
    elif len(image.shape) == 3:
        hist_b = oneCanalHist(image[:,:,0])  # Canal bleu
        hist_g = oneCanalHist(image[:,:,1])  # Canal vert
        hist_r = oneCanalHist(image[:,:,2])  # Canal rouge
        return hist_b, hist_g, hist_r
    

# Afficher l'histogramme d'une image
def show_hist(image):
    hist_b, hist_g, hist_r = calculer_histogramme(image)

    # Afficher l'histogramme
    plt.figure(figsize=(10, 5))

    if hist_g is None and hist_r is None:  # Image en niveaux de gris
        plt.plot(hist_b, color='black')
        plt.title("Histogramme - Image en niveaux de gris")
        plt.xlabel("Intensité de pixel")
        plt.ylabel("Nombre de pixels")
    else:  # Image en couleur
        plt.plot(hist_b, color='blue', label='Canal bleu')
        plt.plot(hist_g, color='green', label='Canal vert')
        plt.plot(hist_r, color='red', label='Canal rouge')
        plt.title("Histogramme - Image en couleur")
        plt.xlabel("Pixel")
        plt.ylabel("Intensité de pixel")
        plt.legend()

    plt.show()