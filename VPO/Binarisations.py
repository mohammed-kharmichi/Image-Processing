import cv2  # type: ignore
import numpy as np # type: ignore

 # Binarisation global manual
def binarisation_globale_manual(image, seuil):
    # Vérifier si l'image est en niveaux de gris
    if len(image.shape) == 3 and image.shape[2] == 3:
        # Convertir l'image en niveaux de gris
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif len(image.shape) == 2:
        # L'image est déjà en niveaux de gris
        image_gray = image
    else:
        raise ValueError("L'image n'est ni en niveaux de gris ni en couleurs (BGR)")

    # Binariser l'image en fonction du seuil
    binarisee = np.where(image_gray > seuil, 255, 0).astype(np.uint8)
    
    return binarisee


# Trouver le suil d'otsu optimale
def otsu_threshold(image):
    # Convert the image to grayscale if it's not already
    gray = image
    if len(image.shape) == 3 and image.shape[2] == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the histogram of the image
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # normalize hitogram
    hist_norm = hist.ravel() / hist.sum()
    
    # Calculate the cumulative means and prob
    m = np.cumsum(hist_norm)
    mean = np.cumsum(hist_norm * np.arange(256))
    
    # Find the optimal threshold (Otsu's threshold)
    optimal_thresh = 0
    max_sigma_inter = 0
    for i in range(256):
        if m[i] != 0 and m[i] != 1:
            sigma_inter = (mean[-1] * m[i] - mean[i])**2 / (m[i] * (1 - m[i]))
            if sigma_inter > max_sigma_inter:
                max_sigma_inter = sigma_inter
                optimal_thresh = i
    
    return optimal_thresh

# Binarisation globale par seuil d'otsu
def binarisation_globale_otsu(image):
    seuil = otsu_threshold(image)
    image_binarisee = binarisation_globale_manual(image, seuil)
    return image_binarisee