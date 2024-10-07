import cv2  # type: ignore

def save_image(image, output_path):
    # Liste des extensions supportées
    supported_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif"]
    
    # Vérifier si output_path se termine par une extension supportée
    if not any(output_path.lower().endswith(ext) for ext in supported_extensions):
        # Ajouter l'extension par défaut .png si aucune extension supportée n'est trouvée
        output_path += ".png"
    
    # Sauvegarder l'image
    cv2.imwrite(output_path, image)