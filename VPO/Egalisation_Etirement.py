from VPO.BaseFunctions import calculer_histogramme # type: ignore
import numpy as np # type: ignore
import cv2  # type: ignore

# Égaliser une image
def egaliser_image(image):      # fonction à modifier pour le cas de rgb
    # Calculer l'histogramme de l'image
    hist, _, _ = calculer_histogramme(image)
    total_pixels = np.sum(hist)
    
    # Normaliser l'histogramme
    hist_normalized = hist / total_pixels
    
    # Calculer la somme cumulative des densités
    cdf = np.cumsum(hist_normalized)
    
    # Appliquer la transformation
    if len(image.shape) == 2:  # Image en niveaux de gris
        height, width = image.shape
        egalisee = np.zeros_like(image)
        for y in range(height):
            for x in range(width):
                intensity = image[y, x]
                egalisee[y, x] = cdf[intensity] * 255
    elif len(image.shape) == 3:  # Image en couleur
        height, width, channels = image.shape
        egalisee = np.zeros_like(image)
        for y in range(height):
            for x in range(width):
                for c in range(channels):
                    intensity = image[y, x, c]
                    egalisee[y, x, c] = cdf[intensity] * 255
    
    return egalisee.astype(np.uint8)


# Etirer une image
def etirer_image(image):
    # Pour les images en niveaux de gris
    if len(image.shape) == 2:
        # Trouver les valeurs min et max des pixels
        min_val = np.min(image)
        max_val = np.max(image)
        
        # Étirer le contraste en appliquant la transformation linéaire
        etiree = (image - min_val) * (255 / (max_val - min_val))
        
        return etiree.astype(np.uint8)
    
    # Pour les images couleur
    elif len(image.shape) == 3:
        etiree_channels = []
        for channel in cv2.split(image):
            # Trouver les valeurs min et max des pixels pour chaque canal de couleur
            min_val = np.min(channel)
            max_val = np.max(channel)
            
            # Étirer le contraste en appliquant la transformation linéaire à chaque canal
            etiree_channel = (channel - min_val) * (255 / (max_val - min_val))
            etiree_channels.append(etiree_channel)
        
        # Fusionner les canaux étirés pour former l'image couleur étirée
        etiree_image = cv2.merge(etiree_channels)
        
        return etiree_image.astype(np.uint8)