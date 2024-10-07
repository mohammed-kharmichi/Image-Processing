import cv2  # type: ignore
import numpy as np # type: ignore

# Transformations de fourrier
def Fourier(image):
    # Appliquer la transformation de Fourier
    fourier_transform = np.fft.fft2(image)

    # Centrer le spectre
    fourier_transform_shift = np.fft.fftshift(fourier_transform)
    return fourier_transform_shift

def FourierInverse(fourier_transform_shift):
    f_ishift = np.fft.ifftshift(fourier_transform_shift)
    filtered_image = np.fft.ifft2(f_ishift)
    filtered_image = np.abs(filtered_image)
    return filtered_image 

# Filtres passe bas

# Filtre ideal
def getBasIdealFilter(image, seuil):

    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    transforme_fourrier = Fourier(image) # obtenir les spectres

    rows, cols = transforme_fourrier.shape[:2]
    centerRow, centerCol = rows // 2, cols // 2
    
    # je crée un masque vide car je considere au debut que tous les fréquences sont des hautes fréquences
    filtre = np.zeros((rows, cols), np.uint8) 
    
    # je calcule la distance par rapport au centre de la transformation
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - centerRow) ** 2 + (j - centerCol) ** 2)
            if dist <= seuil: # si un emplacement de fréquence vérifie ce condition
                filtre[i, j] = 1 # je le considere comme basse fréquence
    
    transforme_fourrier = transforme_fourrier*filtre
                
    return FourierInverse(transforme_fourrier)

# Filtre ButterWorth
def getBasButterWorthFilter(image, seuil, ordre):

    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    transforme_fourrier = Fourier(image) # obtenir les spectres

    rows, cols = transforme_fourrier.shape[:2]
    centerRow, centerCol = rows // 2, cols // 2
    filtre = np.zeros((rows, cols), np.float64)
    
    # je traverse chaque frequence de la transformation de fourrier
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - centerRow) ** 2 + (j - centerCol) ** 2)
            filtre[i, j] = 1/(1+(dist/seuil)**(2*ordre))

    transforme_fourrier = transforme_fourrier*filtre
                
    return FourierInverse(transforme_fourrier)

# Filtre Gaussien
def getBasGaussienFilter(image, seuil):

    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    transforme_fourrier = Fourier(image) # obtenir les spectres
    
    rows, cols = transforme_fourrier.shape[:2]
    centerRow, centerCol = rows // 2, cols // 2
    filtre = np.zeros((rows, cols), np.float64)
    
    # je traverse chaque frequence de la transformation de fourrier
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - centerRow) ** 2 + (j - centerCol) ** 2)
            filtre[i, j] = np.exp(-dist**2/(2*(seuil**2)))
                
    transforme_fourrier = transforme_fourrier*filtre
                
    return FourierInverse(transforme_fourrier)

# Filtres passe haut

# Filtre ideal
def getHautIdealFilter(image, seuil):

    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    transforme_fourrier = Fourier(image) # obtenir les spectres

    rows, cols = transforme_fourrier.shape[:2]
    centerRow, centerCol = rows // 2, cols // 2
    
    # Créer un masque vide car initialement, toutes les fréquences sont considérées comme basses fréquences
    filtre = np.zeros((rows, cols), np.uint8) 
    
    # Calculer la distance par rapport au centre de la transformation
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - centerRow) ** 2 + (j - centerCol) ** 2)
            if dist > seuil:  # Si une fréquence est au-delà du seuil, elle est considérée comme haute fréquence
                filtre[i, j] = 1  # Considérer comme haute fréquence
                
    transforme_fourrier = transforme_fourrier*filtre
                
    return FourierInverse(transforme_fourrier)

# Filter ButterWorth
def getHautButterWorthFilter(image, seuil, ordre):
    
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    transforme_fourrier = Fourier(image) # obtenir les spectres

    rows, cols = transforme_fourrier.shape[:2]
    centerRow, centerCol = rows // 2, cols // 2
    filtre = np.zeros((rows, cols), np.float64) 
    
    # je traverse chaque frequence de la transformation de fourrier
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - centerRow) ** 2 + (j - centerCol) ** 2)
            filtre[i, j] = 1/(1+(seuil/dist)**(2*ordre))
                
    transforme_fourrier = transforme_fourrier*filtre
                
    return FourierInverse(transforme_fourrier)

# Filtre Gaussien
def getHautGaussienFilter(image, seuil):
    
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    transforme_fourrier = Fourier(image) # obtenir les spectres

    rows, cols = transforme_fourrier.shape[:2]
    centerRow, centerCol = rows // 2, cols // 2
    filtre = np.zeros((rows, cols), np.float64) 
    
    # je traverse chaque frequence de la transformation de fourrier
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - centerRow) ** 2 + (j - centerCol) ** 2)
            filtre[i, j] = 1-np.exp(-dist**2/(2*(seuil**2)))
                
    transforme_fourrier = transforme_fourrier*filtre
                
    return FourierInverse(transforme_fourrier)




