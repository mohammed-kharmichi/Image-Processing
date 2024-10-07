import numpy as np  # type: ignore
import cv2  # type: ignore
from sklearn.cluster import KMeans  # type: ignore

# Méthode de croissance des régions
def region_Croissance(image, seeds, threshold):

    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Initialiser l'image segmentée avec des zéros
    segmented_image = np.zeros_like(image, dtype=np.uint8)
    
    # Récupérer les dimensions de l'image
    rows, cols = image.shape
    
    # Créer une liste pour stocker les pixels à examiner
    pixels_to_check = seeds[:]
    
    # Tant qu'il y a des pixels à examiner
    while pixels_to_check:
        # Récupérer le prochain pixel à examiner
        current_pixel = pixels_to_check.pop(0)
        
        # Vérifier si le pixel a déjà été examiné
        if segmented_image[current_pixel] == 0:
            # Vérifier si la valeur du pixel est similaire à celle des graines
            for seed in seeds:
                if abs(int(image[current_pixel]) - int(image[seed])) < threshold:
                    # Ajouter le pixel à l'image segmentée
                    segmented_image[current_pixel] = 255
                    
                    # Ajouter les pixels voisins à la liste des pixels à examiner
                    if current_pixel[0] + 1 < rows:
                        pixels_to_check.append((current_pixel[0] + 1, current_pixel[1]))
                    if current_pixel[0] - 1 >= 0:
                        pixels_to_check.append((current_pixel[0] - 1, current_pixel[1]))
                    if current_pixel[1] + 1 < cols:
                        pixels_to_check.append((current_pixel[0], current_pixel[1] + 1))
                    if current_pixel[1] - 1 >= 0:
                        pixels_to_check.append((current_pixel[0], current_pixel[1] - 1))
    
    return segmented_image


def k_means_Segmentation(image, k):

    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convertir l'image en un tableau numpy 1D
    pixels = image.reshape((-1, 2))

    # Créer un objet KMeans avec k clusters
    kmeans = KMeans(n_clusters=k)

    # Effectuer le clustering sur les pixels de l'image
    kmeans.fit(pixels)

    # Récupérer les labels des clusters et les centres
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    # Assigner chaque pixel à un cluster en utilisant les labels
    segmented_image = centers[labels].astype(np.uint8)
                                                                          
    # Remettre l'image à sa forme d'origine
    segmented_image = segmented_image.reshape(image.shape)

    return segmented_image