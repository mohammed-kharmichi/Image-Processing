import numpy as np # type: ignore
import cv2  # type: ignore
from scipy.signal import convolve2d  # type: ignore

# Appliquer le filtre Gaussien (en spécifiant une valeur pour l’écart type)
def filtre_gaussien(image, ecartType, taille):
    # Initialisation du filtre gaussien
    S = np.floor(taille / 2).astype(int)
    filtre = np.zeros((taille, taille))
    C = 1 / (2 * np.pi * ecartType**2)
    K = 2 * ecartType**2

    for i in range(-S, S+1):
        for j in range(-S, S+1):
            filtre[i+S, j+S] = C * np.exp(-(i**2 + j**2) / K)

    # Normalisation du filtre
    filtre /= np.sum(filtre)

    # Vérification si l'image est en niveaux de gris ou en couleur
    if len(image.shape) == 2:  # Niveaux de gris
        # Application du filtre à l'image
        image_filtree = convolve2d(image, filtre, mode='same', boundary='symm')

    elif len(image.shape) == 3:  # Couleur
        # Application du filtre à chaque canal de l'image
        image_filtree = np.zeros_like(image, dtype=np.float32)
        for channel in range(image.shape[2]):
            image_filtree[:,:,channel] = convolve2d(image[:,:,channel], filtre, mode='same', boundary='symm')

    return image_filtree.astype(np.uint8)


# Appliquer le filtre moyenneur sur une canal
def appliquer_filtre_moyenneur_sur_canal(channel, taille_filtre):
    height, width = channel.shape[:2]
    channel_filtre = np.zeros_like(channel, dtype=np.float32)
    
    # Calculer le padding pour la convolution
    padding = taille_filtre // 2

    for y in range(height):
        for x in range(width):
            # Extraire la fenêtre centrée sur le pixel actuel
            window = channel[max(y - padding, 0):min(y + padding + 1, height), max(x - padding, 0):min(x + padding + 1, width)]
            # Calculer la moyenne de la fenêtre
            mean_val = np.mean(window)
            # Affecter la moyenne au pixel correspondant dans l'image filtrée
            channel_filtre[y, x] = mean_val

    return channel_filtre.astype(np.uint8)

# Appliquer le filtre moyenneur sur une image
def filtre_moyenneur(image, taille_filtre):
    # Vérification si l'image est en niveaux de gris ou en couleur
    if len(image.shape) == 2:  # Niveaux de gris
        image_filtree = appliquer_filtre_moyenneur_sur_canal(image, taille_filtre)
        
    elif len(image.shape) == 3:  # Couleur
        channels_filtres = []
        for channel in cv2.split(image):
            channel_filtree = appliquer_filtre_moyenneur_sur_canal(channel, taille_filtre)
            channels_filtres.append(channel_filtree)
        image_filtree = cv2.merge(channels_filtres)
        
    return image_filtree


# Appliquer le filtre médian sur une image
def filtre_median(image, taille):

    if len(image.shape) == 2:  # Image en niveaux de gris
        nblg, nbcolonne = image.shape
        ImageFinale = np.zeros_like(image, dtype=np.uint8)

        S = taille // 2

        for i in range(1+S, nblg-S):
            for j in range(1+S, nbcolonne-S):
                fenetre = image[i-S:i+S+1, j-S:j+S+1]
                ImageFinale[i, j] = np.median(fenetre)

    else:  # Image en couleur
        nblg, nbcolonne, _ = image.shape
        ImageFinale = np.zeros_like(image, dtype=np.uint8)

        S = taille // 2

        for i in range(1+S, nblg-S):
            for j in range(1+S, nbcolonne-S):
                fenetre = image[i-S:i+S+1, j-S:j+S+1, :]
                for k in range(3):  # Parcourir les canaux de couleur
                    ImageFinale[i, j, k] = np.median(fenetre[:, :, k])

    
    return ImageFinale
