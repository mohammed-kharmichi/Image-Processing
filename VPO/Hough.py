from VPO.Contours_Extraction import sobel_operator
import numpy as np  # type: ignore


def hough_transform(image, threshold):
    
    # Prétraitement de l'image (détection de contours avec la méthode Sobel)
    edges = sobel_operator(image)
    
    # Définir l'espace de paramètres de la transformation de Hough
    height, width = edges.shape
    max_rho = int(np.ceil(np.sqrt(height**2 + width**2)))
    thetas = np.deg2rad(np.arange(-90, 90))
    num_thetas = len(thetas)
    
    # Initialiser l'accumulateur de votes
    accumulator = np.zeros((2 * max_rho, num_thetas), dtype=int)
    
    # Parcourir l'image pour voter pour les lignes possibles
    edge_pixels = np.argwhere(edges >= threshold)
    for y, x in edge_pixels:
        for t_idx, theta in enumerate(thetas):
            rho = int(x * np.cos(theta) + y * np.sin(theta))
            accumulator[rho + max_rho, t_idx] += 1
    
    # Trouver les lignes ayant un nombre de votes supérieur au seuil
    lines = np.argwhere(accumulator >= threshold)
    
    return lines
