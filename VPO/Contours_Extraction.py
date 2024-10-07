import numpy as np  # type: ignore
import cv2 # type: ignore
import os 

# Methode Basée sur les filtres de Sobel
def sobel_operator(image):
    
    if len(image.shape)>2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Définition des masques de Sobel pour la détection des contours en x et y
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    
    sobel_y = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])
    
    # Initialisation des matrices de gradients en x et y
    gradient_x = np.zeros_like(image, dtype=np.float32)
    gradient_y = np.zeros_like(image, dtype=np.float32)
    
    # Convolution de l'image avec les masques de Sobel pour obtenir les gradients
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            gradient_x[i, j] = np.sum(image[i-1:i+2, j-1:j+2] * sobel_x)
            gradient_y[i, j] = np.sum(image[i-1:i+2, j-1:j+2] * sobel_y)
    
    # Calcul du gradient total (magnitude) en combinant les gradients en x et y
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    
    return gradient_magnitude

# Detection de contours par application de filtre de laplacien ( dérivée de seconde ordre )
def laplacian_operator(image):

    if len(image.shape)>2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    # Définition du masque de Laplace
    laplacian_mask = np.array([[0, 1, 0], # cette filtre ne donne pas d'importance au point de centre
                               [1, -4, 1],
                               [0, 1, 0]])
    
    # laplacian_mask = np.array([[0, -1, 0], # cette filtre ne donne un importance au point de centre
    #                            [-1, 4, -1],
    #                            [0, -1, 0]])
    

    # Initialisation de la matrice du résultat
    laplacian_result = np.zeros_like(image, dtype=np.float32)
    
    # Convolution de l'image avec le masque de Laplace
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            laplacian_result[i, j] = np.sum(image[i-1:i+2, j-1:j+2] * laplacian_mask)
    
    return laplacian_result

# Methode basée sur les filtres de Robert
def robert_operator(image):

    if len(image.shape)>2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Définition des masques de Robert pour la détection des contours en diagonale
    robert_mask1 = np.array([[1, 0],
                             [0, -1]])
    
    robert_mask2 = np.array([[0, 1],
                             [-1, 0]])
    
    # Initialisation des matrices de gradients
    gradient1 = np.zeros_like(image, dtype=np.float32)
    gradient2 = np.zeros_like(image, dtype=np.float32)
    
    # Convolution de l'image avec les masques de Robert pour obtenir les gradients
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            gradient1[i, j] = np.sum(image[i-1:i+1, j-1:j+1] * robert_mask1)
            gradient2[i, j] = np.sum(image[i-1:i+1, j-1:j+1] * robert_mask2)
    
    # Calcul du gradient total (magnitude) en combinant les gradients obtenus
    gradient_magnitude = np.sqrt(gradient1**2 + gradient2**2)
    
    return gradient_magnitude

