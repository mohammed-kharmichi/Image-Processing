from VPO.BaseFunctions import *
from VPO.Binarisations import *
from VPO.Egalisation_Etirement import *
from VPO.Spatial_Filters import *
from VPO.Frequentiel_Filters import *
from VPO.Morphologie_Mathématique import *
from VPO.Contours_Extraction import *
from VPO.Image_Segmentation import *
from VPO.Hough import hough_transform
from VPO.Compression import *
from VPO.SaveImage import save_image
from VPO.Compression import *
from PyQt5.QtWidgets import QFileDialog # type: ignore
from PyQt5.QtGui import QImage, QPixmap # type: ignore
from PyQt5 import QtCore  # type: ignore


# Pour styler les bottins de gauche
def left_style(ui):
    menu_item_style = """
        color: white;
        font-size: 12px;
        padding-left: 15%;
    }

    QWidget#left_menu_center_part QLabel:hover {
        color: black;
        background-color: white;
    }
    """
    ui.left_menu_base_actions.setStyleSheet("#left_menu_base_actions {" + menu_item_style)
    ui.left_menu_binarization.setStyleSheet("#left_menu_binarization {" + menu_item_style)
    ui.left_menu_filters.setStyleSheet("#left_menu_filters {" + menu_item_style)
    ui.left_menu_frequency_feltring.setStyleSheet("#left_menu_frequency_feltring {" + menu_item_style)
    ui.left_menu_contours.setStyleSheet("#left_menu_contours {" + menu_item_style)
    ui.left_menu_morphology.setStyleSheet("#left_menu_morphology {" + menu_item_style)
    ui.left_menu_segmentation.setStyleSheet("#left_menu_segmentation {" + menu_item_style)
    ui.left_menu_points_of_interest.setStyleSheet("#left_menu_points_of_interest {" + menu_item_style)
    ui.left_menu_compression.setStyleSheet("#left_menu_compression {" + menu_item_style)
    ui.left_menu_save_image.setStyleSheet("""
                                            #left_menu_save_image {
                                                color: white;
                                                font-size: 12px;
                                                padding-left: 15%;
                                                max-height: 30px;
                                            }
                                            #left_menu_save_image:hover {
                                                color: black;
                                                background-color: white;
                                            }
                                        """)

# this function is to style the top menu labels 
def apply_label_style(label):
    label.setStyleSheet("""
        QLabel {
            height: 30px;
            padding: 4px 20px;
        }
        QLabel:hover {
            background-color: white;
        }
    """)
        
# this function to apply style on top labels
def top_style(ui):
    apply_label_style(ui.inverse_image)
    apply_label_style(ui.resize_image)
    apply_label_style(ui.equalize)
    apply_label_style(ui.rotate_image)
    apply_label_style(ui.histogramme)
    apply_label_style(ui.stretch)
    
    apply_label_style(ui.manual_thresholding)
    apply_label_style(ui.otsu_thresholding)
    
    apply_label_style(ui.gaussien)
    apply_label_style(ui.mean)
    apply_label_style(ui.median)
    
    apply_label_style(ui.ideal)
    apply_label_style(ui.butterworth)
    apply_label_style(ui.gauss)

    apply_label_style(ui.sobel)
    apply_label_style(ui.robert)
    apply_label_style(ui.laplacien)
    apply_label_style(ui.gradiant)
    
    apply_label_style(ui.erosion)
    apply_label_style(ui.dilatation)
    apply_label_style(ui.ouverture)
    apply_label_style(ui.fermeture)

    apply_label_style(ui.kmeans)
    apply_label_style(ui.region_croissance)
    apply_label_style(ui.regions_partition)

    apply_label_style(ui.hough)

    apply_label_style(ui.huffman)
    apply_label_style(ui.lzw)

# To hide main body bottom elements
def remove_main_body_bottom_elements(ui):
    ui.main_body_bottom_part_rotate_image.hide()
    ui.main_body_bottom_part_resize_image.hide()
    ui.main_body_bottom_part_otsu_threshold.hide()
    ui.main_body_bottom_part_manual_threshold.hide()
    ui.main_body_bottom_part_mean.hide()
    ui.main_body_bottom_part_median.hide()
    ui.main_body_bottom_part_gaussien.hide()
    ui.main_body_bottom_part_frequency_filtring_ideal.hide()
    ui.main_body_bottom_part_frequency_filtring_gaussien.hide()
    ui.main_body_bottom_part_frequency_filtring_butterworth.hide()
    ui.main_body_bottom_part_erosion.hide()
    ui.main_body_bottom_part_dilatation.hide()
    ui.main_body_bottom_part_ouverture.hide()
    ui.main_body_bottom_part_fermeture.hide()

    ui.main_body_bottom_part_kmeans.hide()
    ui.main_body_bottom_part_region_croissance.hide()

    ui.main_body_bottom_part_hough.hide()
    ui.main_body_bottom_part_huffman.hide()
    

# To hide main body top elements
def hide_top_parts(ui):
    ui.main_body_top_part_binarization.hide()
    ui.main_body_top_part_base_actions.hide()
    ui.main_body_top_part_filters.hide()
    ui.main_body_top_part_frequency_filters.hide()
    ui.main_body_top_part_contours.hide()
    ui.main_body_top_part_morphology.hide()
    ui.main_body_top_part_segmentation.hide()
    ui.main_body_top_part_points_of_interest.hide()
    ui.main_body_top_part_compression.hide()

# open the file explorer
def open_file_dialog(ui):
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.tif)")
    file_dialog.setViewMode(QFileDialog.Detail)
    if file_dialog.exec_():
        original_image_path = file_dialog.selectedFiles()[0]
        original_image = read_image(original_image_path)
        return original_image
    else:
        return None
    
# sauvegarder une image
def save_file_dialog(ui, image):
    # Ouvrir le dialog de sauvegarde de fichier et attendre que l'utilisateur sélectionne un fichier
    options = QFileDialog.Options()
    file_filter = "Image Files (*.png *.jpg *.jpeg *.bmp *.tif)"
    file_name, _ = QFileDialog.getSaveFileName(None, "Save File", "", file_filter, options=options)
    
    # Si un fichier est sélectionné, afficher son nom dans le label
    if file_name:
        print(file_name)
        save_image(image, file_name)

# def show_image(ui, image):
#     if image is not None:
#         ui.image_place.show()

#         if len(image.shape) == 2:  # Image en niveaux de gris
#             height, width = image.shape
#             bytesPerLine = width * 1  # Image en niveaux de gris a seulement 1 canal
#             image_bytes = image.tobytes()  # Convertir les données de l'image en octets
#             qImg = QImage(image_bytes, width, height, bytesPerLine, QImage.Format_Grayscale8)

#         elif len(image.shape) == 3:  # Image RGB
#             # Si l'image est en BGR (comme c'est souvent le cas avec OpenCV), la convertir en RGB
#             if image.shape[2] == 3:
#                 image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             height, width, channel = image.shape
#             bytesPerLine = width * channel
#             image_bytes = image.tobytes()  # Convertir les données de l'image en octets
#             qImg = QImage(image_bytes, width, height, bytesPerLine, QImage.Format_RGB888)

#         pixmap = QPixmap.fromImage(qImg)
#         ui.image_place.setPixmap(pixmap)

#         # Ajuster la taille et la position de l'image pour s'adapter à la partie centrale du corps principal
#         width = min(width, ui.main_body_center_part.width())
#         height = min(height, 604 - 120)
#         ui.image_place.setGeometry(QtCore.QRect((ui.main_body_center_part.width() - width) // 2,
#                                                 (ui.main_body_center_part.height() - height) // 2, width, height))


def show_image(ui, image):
    if image is not None:
        ui.image_place.show()

        if len(image.shape) == 2:  # Image en niveaux de gris
            height, width = image.shape
            bytesPerLine = width * 1  # Image en niveaux de gris a seulement 1 canal
            # Convertir les données de l'image en bytes
            image_bytes = image.astype(np.uint8).tobytes()
            qImg = QImage(image_bytes, width, height, bytesPerLine, QImage.Format_Grayscale8)

        elif len(image.shape) == 3:  # Image RGB
            if image.shape[2] == 3:
                # Convertir de BGR à RGB si nécessaire
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            bytesPerLine = width * channel
            # Convertir les données de l'image en bytes
            image_bytes = image.astype(np.uint8).tobytes()
            qImg = QImage(image_bytes, width, height, bytesPerLine, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(qImg)
        ui.image_place.setPixmap(pixmap)

        # Ajuster la taille de l'image pour s'adapter à la zone d'affichage
        width = min(width, ui.main_body_center_part.width())
        height = min(height, ui.main_body_center_part.height())
        ui.image_place.setScaledContents(True)  # Redimensionner l'image pour s'adapter à la zone d'affichage
        ui.image_place.setGeometry(QtCore.QRect((ui.main_body_center_part.width() - width) // 2,
                                                (ui.main_body_center_part.height() - height) // 2, width, height))


# Appliquer le style sur les bottons de droite
def original_image_style(ui):
    ui.image_original.setStyleSheet("""
        #image_original {
            font-size: 12px;
            padding-left: 9%;
            padding-top: 2px;
            padding-bottom: 2px;
            color: black;   
            background-color: white;}
                                """)
    ui.image_current.setStyleSheet("""
        #image_current {
            color: white;   
            font-size: 12px;
            padding-left: 9%;    
            padding-top: 2px;
            padding-bottom: 2px;}
        #image_current:hover {
                color: black;  background-color: white;}
                                    """)

def current_image_style(ui):
    ui.image_original.setStyleSheet("""
        #image_original {
            color: white;   
            font-size: 12px;
            padding-left: 9%;    
            padding-top: 2px;
            padding-bottom: 2px;}
        #image_original:hover {
                color: black;  background-color: white;}
                                    """)
    ui.image_current.setStyleSheet("""
        #image_current {
            font-size: 12px;
            padding-left: 9%;
            padding-top: 2px;
            padding-bottom: 2px;
            color: black;   
            background-color: white;}
                                """)
    
#################### Afficher les elements de base actions ##########################
def show_base_actions_elements(ui):
    left_style(ui)
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    hide_top_parts(ui)
    ui.main_body_top_part_base_actions.show()
    ui.left_menu_base_actions.setStyleSheet("#left_menu_base_actions {\n"
                                                "font-size: 12px;\n"
                                                "color:black;\n"
                                                "padding-left: 15%;\n"
                                                "background-color: white;\n"
                                                "}\n" )
    
# inverse image
def inverse_current_image(ui, image):
    remove_main_body_bottom_elements(ui)
    top_style(ui)
    inversed_image = negative_image(image)
    ui.inverse_image.setStyleSheet("#inverse_image {\n"
                                                        "color:black;\n"
                                                        "background-color: white;\n"
                                                        "height: 30px;\n"
                                                        "    padding: 4px 20px;\n"
                                                        "}\n" )
    return inversed_image
    
# show rotate image elements
def show_rotate_image_elements(ui):
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_rotate_image.show()
    top_style(ui)
    ui.rotate_image.setStyleSheet("#rotate_image {\n"
                                                    "color:black;\n"
                                                    "background-color: white;\n"
                                                    "height: 30px;\n"
                                                    "padding: 4px 20px;\n"
                                                    "}\n" )


# rotate image
def rotate_current_image(ui, image):
    rotation_value = ui.rotation_angle.value()
    current_image_version = rotate_image(image, rotation_value)
    return current_image_version

# show resize image elements
def show_resize_image_elements(ui):
    remove_main_body_bottom_elements(ui)
    top_style(ui)
    ui.main_body_bottom_part_resize_image.show()
    ui.resize_image.setStyleSheet("#resize_image {\n"
                                                    "color:black;\n"
                                                    "background-color: white;\n"
                                                    "height: 30px;\n"
                                                    "padding: 4px 20px;\n"
                                                    "}\n" )
        
def resize_image_with_percentage(ui, image):
    percentage = ui.percentage.value()
    current_image_version = resize_image(image, None, percentage)
    return current_image_version
    
def resize_image_with_width_height(ui, image):
    width = ui.width.value()
    height = ui.height.value()
    current_image_version = resize_image(image, (height, width), None)
    return current_image_version

# Afficher l'histogramme
def show_histogram(ui, image):
    remove_main_body_bottom_elements(ui)
    top_style(ui)
    show_hist(image)
    ui.histogramme.setStyleSheet("#histogramme {\n"
                                                    "color:black;\n"
                                                    "background-color: white;\n"
                                                    "height: 30px;\n"
                                                    "padding: 4px 20px;\n"
                                                    "}\n" )
    
#h Egaliser une image
def equalized_image(ui, image):
    remove_main_body_bottom_elements(ui)
    top_style(ui)
    current_image = egaliser_image(image)
    ui.equalize.setStyleSheet("#equalize {\n"
                                                    "color:black;\n"
                                                    "background-color: white;\n"
                                                    "height: 30px;\n"
                                                    "padding: 4px 20px;\n"
                                                    "}\n" )
    return current_image
    
# etirer une image
def stretched_image(ui, image):
    remove_main_body_bottom_elements(ui)
    top_style(ui)
    ui.stretch.setStyleSheet("#stretch {\n"
                                            "color:black;\n"
                                            "background-color: white;\n"
                                            "height: 30px;\n"
                                            "padding: 4px 20px;\n"
                                            "}\n" )
    current_image = etirer_image(image)
    return current_image

             

########################## Afficher les elements de binarization #########################
def show_binarization_elements(ui):
    left_style(ui)
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    hide_top_parts(ui)
    ui.main_body_top_part_binarization.show()
    ui.left_menu_binarization.setStyleSheet("#left_menu_binarization {\n"
                                                "font-size: 12px;\n"
                                                "color:black;\n"
                                                "padding-left: 15%;\n"
                                                "background-color: white;\n"
                                                "}\n" )
    
# binarization d'otsu
def apply_otsu_thresholding(ui, image):
    remove_main_body_bottom_elements(ui)
    top_style(ui)
    seuil = otsu_threshold(image)
    ui.otsu_threshold_value.setText(str(seuil))
    ui.main_body_bottom_part_otsu_threshold.show()
    ui.otsu_thresholding.setStyleSheet("#otsu_thresholding {\n"
                                                    "color:black;\n"
                                                    "background-color: white;\n"
                                                    "height: 30px;\n"
                                                    "padding: 4px 20px;\n"
                                                    "}\n" )
    current_image_version = binarisation_globale_otsu(image)
    return current_image_version

# show manual thresholding elements
def show_manual_thresholding(ui):
    remove_main_body_bottom_elements(ui)
    top_style(ui)
    ui.main_body_bottom_part_manual_threshold.show()
    ui.manual_thresholding.setStyleSheet("#manual_thresholding {\n"
                                                    "color:black;\n"
                                                    "background-color: white;\n"
                                                    "height: 30px;\n"
                                                    "padding: 4px 20px;\n"
                                                    "}\n" )

# binarisation manual
def apply_manual_thresholding(ui, image):
    seuil = ui.otsu_manual_threshold.value()
    current_image = binarisation_globale_manual(image, seuil)
    return current_image
    
##################################### Afficher les elements de Filters #########################
def show_filters_elements(ui):
    left_style(ui)
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    hide_top_parts(ui)
    ui.main_body_top_part_filters.show()
    ui.left_menu_filters.setStyleSheet("#left_menu_filters {\n"
                                                "font-size: 12px;\n"
                                                "color:black;\n"
                                                "padding-left: 15%;\n"
                                                "background-color: white;\n"
                                                "}\n" )

# show mean bottom elements
def show_mean_bottom_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_mean.show()
    ui.mean.setStyleSheet("#mean {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )

# show median bottom elements
def show_median_bottom_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_median.show()
    ui.median.setStyleSheet("#median {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )

# show gaussien bottom elements
def show_gaussien_bottom_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_gaussien.show()
    ui.gaussien.setStyleSheet("#gaussien {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )

# Apply mean filter
def apply_filter_mean(ui, image):
    taille = ui.taille_mean_filter.value()
    current_image_version = filtre_moyenneur(image, taille)
    return current_image_version

# Apply median filter
def apply_filter_median(ui, image):
    taille = ui.taille_median_filter.value()
    current_image_version = filtre_median(image, taille)
    return current_image_version

# Apply gaussien filter
def apply_filter_gaussien(ui, image):
    ecartType = ui.ecartType_gaussien_filter.value()
    taille = ui.taille_gaussien_filter.value()
    current_image_version = filtre_gaussien(image, ecartType, taille)
    return current_image_version
   

#################################### Afficher les elements de FrequencyFeltring #############################
def show_frequency_filters_elements(ui):
    left_style(ui)
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    hide_top_parts(ui)
    ui.main_body_top_part_frequency_filters.show()
    ui.left_menu_frequency_feltring.setStyleSheet("#left_menu_frequency_feltring {\n"
                                                "font-size: 12px;\n"
                                                "color:black;\n"
                                                "padding-left: 15%;\n"
                                                "background-color: white;\n"
                                                "}\n" )
    
# show ideal bottom elements
def show_ideal_bottom_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_frequency_filtring_ideal.show()
    ui.ideal.setStyleSheet("#ideal {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )
    
def applyBasIdealFilter(image, seuil):
    image_filtred = getBasIdealFilter(image, seuil)
    return image_filtred

def applyBasButterWorthFilter(image, seuil, order):
    return getBasButterWorthFilter(image, seuil, order)

def applyBasGaussienFilter(image, seuil):
    return getBasGaussienFilter(image, seuil)

def applyHautIdealFilter(image, seuil):
    return getHautIdealFilter(image, seuil)

def applyHautButterWorthFilter(image, seuil, order):
    return getHautButterWorthFilter(image, seuil, order)

def applyHautGaussienFilter(image, seuil):
    return getHautGaussienFilter(image, seuil)

# show guass bottom elements
def show_gauss_bottom_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_frequency_filtring_gaussien.show()
    ui.gauss.setStyleSheet("#gauss {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )
    
# show guass bottom elements
def show_butterworth_bottom_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_frequency_filtring_butterworth.show()
    ui.butterworth.setStyleSheet("#butterworth {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )
    

#################################### contours #####################################
def show_contours_elements(ui):
    left_style(ui)
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    hide_top_parts(ui)
    ui.main_body_top_part_contours.show()
    ui.left_menu_contours.setStyleSheet("#left_menu_contours {\n"
                                                "font-size: 12px;\n"
                                                "color:black;\n"
                                                "padding-left: 15%;\n"
                                                "background-color: white;\n"
                                                "}\n" )
    
def apply_sobel(image):
    return sobel_operator(image)

def apply_robert(image):
    return robert_operator(image)

def apply_laplacien(image):
    return laplacian_operator(image)
    
#################################### morphologies #####################################
def show_morphology_elements(ui):
    left_style(ui)
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    hide_top_parts(ui)
    ui.main_body_top_part_morphology.show()
    ui.left_menu_morphology.setStyleSheet("#left_menu_morphology {\n"
                                                "font-size: 12px;\n"
                                                "color:black;\n"
                                                "padding-left: 15%;\n"
                                                "background-color: white;\n"
                                                "}\n" )
    
# show erosion elements
def show_erosion_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_erosion.show()
    ui.erosion.setStyleSheet("#erosion {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )

# show dilatation elements
def show_dilatation_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_dilatation.show()
    ui.dilatation.setStyleSheet("#dilatation {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )

# show ouverture elements
def show_ouverture_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_ouverture.show()
    ui.ouverture.setStyleSheet("#ouverture {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )

# show fermeture elements
def show_fermeture_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_fermeture.show()
    ui.fermeture.setStyleSheet("#fermeture {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )
    
# appliquer l'erosion
def applyErosion(image, es):
    image_morph = erosion(image, es)
    return image_morph

# appliquer dilatation
def applyDilatation(image, es):
    image_morph = dilatation(image, es)
    return image_morph

# appliquer fermeture
def applyFermeture(image, es):
    image_morph = fermeture(image, es)
    return image_morph

# appliquer ouverture
def applyOuverture(image, es):
    image_morph = ouverture(image, es)
    return image_morph

###################### Segmentations ###################################

# afficher segmentation methodes
def show_segmentation_elements(ui):
    left_style(ui)
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    hide_top_parts(ui)
    ui.main_body_top_part_segmentation.show()
    ui.left_menu_segmentation.setStyleSheet("#left_menu_segmentation {\n"
                                                "font-size: 12px;\n"
                                                "color:black;\n"
                                                "padding-left: 15%;\n"
                                                "background-color: white;\n"
                                                "}\n" )
    
# show kmeans elements
def show_kmeans_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_kmeans.show()
    ui.kmeans.setStyleSheet("#kmeans {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )
    
# appliquer le kmeans
def applyKmeans(image, k):
    return k_means_Segmentation(image, k)

# show region croissance elements
def show_region_croissance_elements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_region_croissance.show()
    ui.region_croissance.setStyleSheet("#region_croissance {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )
    
# apply region croissance
def applyRegionCroissance(image, list, threshold):
    return region_Croissance(image, list, threshold)

###################### points of interest ###################################

# afficher points of interest methodes
def show_points_of_interest_elements(ui):
    left_style(ui)
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    hide_top_parts(ui)
    ui.main_body_top_part_points_of_interest.show()
    ui.left_menu_points_of_interest.setStyleSheet("#left_menu_points_of_interest {\n"
                                                "font-size: 12px;\n"
                                                "color:black;\n"
                                                "padding-left: 15%;\n"
                                                "background-color: white;\n"
                                                "}\n" )
    
# show hough elements
def showHoughElements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_hough.show()
    ui.hough.setStyleSheet("#hough {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )
    
# apply hough
def applyHough(image, seuil):
    return hough_transform(image, seuil)
    

###################### compression ###################################

# afficher compression methodes
def show_compression_elements(ui):
    left_style(ui)
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    hide_top_parts(ui)
    ui.main_body_top_part_compression.show()
    ui.left_menu_compression.setStyleSheet("#left_menu_compression {\n"
                                                "font-size: 12px;\n"
                                                "color:black;\n"
                                                "padding-left: 15%;\n"
                                                "background-color: white;\n"
                                                "}\n" )
    
# afficher huffman elements
def showHuffmanElements(ui):
    top_style(ui)
    remove_main_body_bottom_elements(ui)
    ui.main_body_bottom_part_huffman.show()
    ui.huffman.setStyleSheet("#huffman {\n"
                                    "color:black;\n"
                                    "background-color: white;\n"
                                    "height: 30px;\n"
                                    "padding: 4px 20px;\n"
                                    "}\n" )
    
# appliquer huffman
def applyHuffman(image, file_name):
    huffman_compression(image, file_name)