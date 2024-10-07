from PyQt5 import QtWidgets # type: ignore
from Interface import Ui_MainWindow
from Traitement import *
from PyQt5.QtWidgets import QPushButton, QDialog, QGridLayout, QCheckBox, QVBoxLayout, QHBoxLayout # type: ignore
import numpy as np # type: ignore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Aouter le style au elements de l'interface
        self.addStyleToLeftButtons()
        self.addStyleToTopButtons()

        # Cacher les elements de l'interface
        self.hideBottomElements()
        self.hideTopElements()
        self.ui.right_menu.hide()

        #=================================================#
        #                    Variables                    #
        #=================================================#
        self.original_image = None
        self.current_image_version = None
        self.checkboxes = None
        self.morph = None
        self.region_croissance_list = None

        #=================================================#
        #       Gestion des evenements de clique          #
        #=================================================#

        # botton load image
        self.ui.load_image.clicked.connect(self.openFileDialog)

        # botton original image
        self.ui.image_original.mousePressEvent = lambda event: self.showOriginalImage()

        # botton current version of image
        self.ui.image_current.mousePressEvent = lambda event: self.showCurrentImageVersion()

        # botton recuperation de l'image principale
        self.ui.image_orig.mousePressEvent = lambda event: self.backToStandard()

        #==================== botton base actions ========================#
        self.ui.left_menu_base_actions.mousePressEvent = lambda event: self.showBaseActionsElements()

        # inverse image
        self.ui.inverse_image.mousePressEvent = lambda event: self.inverseCurrentImage()
        # show rotate image elements
        self.ui.rotate_image.mousePressEvent = lambda event: self.showRotateImageElements()
        # rotate image
        self.ui.button_rotate.clicked.connect(self.rotateImage)
        # show resize image elements
        self.ui.resize_image.mousePressEvent = lambda event: self.showResizeImageElements()
        # resize image with percentage
        self.ui.button_percentage.clicked.connect(self.resizeImagePercentage)
        # resize image with height and width
        self.ui.button_width_height.clicked.connect(self.resizeImageHeightWidth)
        # show histogram
        self.ui.histogramme.mousePressEvent = lambda event: self.showHistogram()
        # equalize image
        self.ui.equalize.mousePressEvent = lambda event: self.equalizeImage()
        # setretch image
        self.ui.stretch.mousePressEvent = lambda event: self.setretchImage()

        #==================== botton binarization =====================#
        self.ui.left_menu_binarization.mousePressEvent = lambda event: self.showBinarizationElements()

        # show manual threshold elements
        self.ui.manual_thresholding.mousePressEvent = lambda event: self.showManualThresholdingElements()
         # apply manual threshold
        self.ui.button_threshold.mousePressEvent = lambda event: self.applyManualThresholding()
        # apply otsu threshold
        self.ui.otsu_thresholding.mousePressEvent = lambda event: self.applyOtsuThresholding()

        #===================== botton filters =========================#
        self.ui.left_menu_filters.mousePressEvent = lambda event: self.showFiltersElements()

        # show gaussien threshold elements
        self.ui.gaussien.mousePressEvent = lambda event: self.showGaussienFilterElements()
        # show median threshold elements
        self.ui.median.mousePressEvent = lambda event: self.showMedianFilterElements()
        # show mean threshold elements
        self.ui.mean.mousePressEvent = lambda event: self.showMeanFilterElements()

        # apply mean filter
        self.ui.button_apply_mean_filter.clicked.connect(self.applyMeanFilter)
        # apply median filter
        self.ui.button_apply_median_filter.clicked.connect(self.applyMedianFilter)
        # apply gaussien filter
        self.ui.button_apply_gaussien_filter.clicked.connect(self.applyGaussienFilter)

        #===================== botton frequency filters ================#
        self.ui.left_menu_frequency_feltring.mousePressEvent = lambda event: self.showFrequencyFeltringElements()

        # show ideal filter elements
        self.ui.ideal.mousePressEvent = lambda event: self.showIdealFilterElements()
        
        # filtre passe bas
        self.ui.apply_passe_bas_ideal_filter.clicked.connect(self.applyBasIdealFilter)
        # filtre passe haut
        self.ui.apply_passe_haut_ideal_filter.clicked.connect(self.applyHautIdealFilter)

        # show gaussien filter elements
        self.ui.gauss.mousePressEvent = lambda event: self.showGaussFilterElements()

        # filtre passe bas
        self.ui.apply_passe_bas_gaussien_filter.clicked.connect(self.applyBasGaussienFilter)
        # filtre passe haut
        self.ui.apply_passe_haut_gaussien_filter.clicked.connect(self.applyHautGaussienFilter)

        # show gaussien filter elements
        self.ui.butterworth.mousePressEvent = lambda event: self.showButterWorthFilterElements()

        # filtre passe bas
        self.ui.apply_passe_bas_butterworth_filter.clicked.connect(self.applyBasButterworthFilter)
        # filtre passe haut
        self.ui.apply_passe_haut_butterworth_filter.clicked.connect(self.applyHautButterworthFilter)


        #===================== botton contours filters ================#
        self.ui.left_menu_contours.mousePressEvent = lambda event: self.showContoursElements()

        # appliquer sobel
        self.ui.sobel.mousePressEvent = lambda event: self.applySobel()
        # appliquer robert
        self.ui.robert.mousePressEvent = lambda event: self.applyRobert()
        # appliquer laplacien
        self.ui.laplacien.mousePressEvent = lambda event: self.applyLaplacien()

        #===================== botton morphology filters ================#
        self.ui.left_menu_morphology.mousePressEvent = lambda event: self.showMorphologyElements()

        # afficher les elements de l'erosion
        self.ui.erosion.mousePressEvent = lambda event: self.showErosionElements()
        # choisir entre le background et le foreground
        self.ui.apply_porphology_erosion.clicked.connect(self.choseEsForErosion)

        # afficher les elements de dilatation
        self.ui.dilatation.mousePressEvent = lambda event: self.showDilatationElements()
        # choisir entre le background et le foreground
        self.ui.apply_porphology_dilatation.clicked.connect(self.choseEsForDilatation)

        # afficher les elements de l'ouverture
        self.ui.ouverture.mousePressEvent = lambda event: self.showOuvertureElements()
        # choisir entre le background et le foreground
        self.ui.apply_porphology_ouverture.clicked.connect(self.choseEsForOuverture)

        # afficher les elements de fermeture
        self.ui.fermeture.mousePressEvent = lambda event: self.showFermetureElements()
        # choisir entre le background et le foreground
        self.ui.apply_porphology_fermeture.clicked.connect(self.choseEsForFermeture)

        #===================== botton segmentation ================#
        self.ui.left_menu_segmentation.mousePressEvent = lambda event: self.showSegmentationElements()

        # afficher les elements de kmeans
        self.ui.kmeans.mousePressEvent = lambda event: self.showKmeansElements()
        # appliquer le kmeans
        self.ui.apply_kmeans.clicked.connect(self.applyKmeans)

        # afficher les elements de kmeans
        self.ui.region_croissance.mousePressEvent = lambda event: self.showRegionCroissanceElements()

        # ajouter un seed
        self.ui.add_region_croissance.clicked.connect(self.addSeed)

        #§ applique le region croissance
        self.ui.apply_region_croissance.clicked.connect(self.applyRegionCroissance)

        #===================== botton points d'interet ================#
        self.ui.left_menu_points_of_interest.mousePressEvent = lambda event: self.showPointsOfInterestElements()

        # afficher les elements de hough
        self.ui.hough.mousePressEvent = lambda event: self.showHoughElements()
        # appliquer hough
        self.ui.apply_hough.clicked.connect(self.applyHough)

        #===================== compression ================#
        self.ui.left_menu_compression.mousePressEvent = lambda event: self.showCompressionElements()

        # afficher les elements de huffman
        self.ui.huffman.mousePressEvent = lambda event: self.showHuffmanElements()
        # appliquer huffman
        self.ui.apply_huffman.clicked.connect(self.applyHuffman)

        #===================== save image ================#
        self.ui.left_menu_save_image.mousePressEvent = lambda event: self.save_image()

    # go back
    def backToStandard(self):
        self.current_image_version = self.original_image
        self.showOriginalImage()

    # afficher les elements de region croissance
    def showRegionCroissanceElements(self):
        self.region_croissance_list = []
        show_region_croissance_elements(self.ui)
        self.showCurrentImageVersion()

    # ajouter un seed
    def addSeed(self):
        y = self.ui.y_region_croissance.value()
        x = self.ui.x_region_croissance.value()
        seed = (y,x)
        self.region_croissance_list.append(seed)
        print(self.region_croissance_list)

    # applique le resion croissance
    def applyRegionCroissance(self):
        seuil = self.ui.threshold_region_croissance.value()
        self.current_image_version = applyRegionCroissance(self.current_image_version, self.region_croissance_list, seuil)
        self.showCurrentImageVersion()

    # Pour appliquer le style sur les bottons de gauche
    def addStyleToLeftButtons(self):
        left_style(self.ui)

    # Appliquer le style commun sur les bottons de haut
    def addStyleToTopButtons(self):
        top_style(self.ui)

    # Cacher les elements de bas
    def hideBottomElements(self):
        remove_main_body_bottom_elements(self.ui)
    
    # Cacher les elements de haut
    def hideTopElements(self):
        hide_top_parts(self.ui)

    # Ouvrire l'exploiteur de fichiers
    def openFileDialog(self):
        self.original_image = open_file_dialog(self.ui)
        self.current_image_version = self.original_image
        self.ui.main_body_center_part.show()
        self.ui.right_menu.show()
        self.ui.load_image.hide()
        self.showOriginalImage()
    
    # Afficher l'image 
    def showImage(self, image):
        show_image(self.ui, image)

    # Afficher l'image d'origine
    def showOriginalImage(self):
        self.showImage(self.original_image)
        original_image_style(self.ui)
        

    # Afficher la derniere modification de l'image
    def showCurrentImageVersion(self):
        if self.current_image_version is not None:
            self.showImage(self.current_image_version)
            current_image_style(self.ui)
        
    # Afficher les elements de base actions
    def showBaseActionsElements(self):
        if self.original_image is not None:
            show_base_actions_elements(self.ui)
            self.showCurrentImageVersion()

    # Afficher les elements de binarization
    def showBinarizationElements(self):
        if self.original_image is not None:
            show_binarization_elements(self.ui)
            self.showCurrentImageVersion()

    # Afficher les elements de Filters
    def showFiltersElements(self):
        if self.original_image is not None:
            show_filters_elements(self.ui)
            self.showCurrentImageVersion()
    
    # Afficher les elements de FrequencyFeltring
    def showFrequencyFeltringElements(self):
        if self.original_image is not None:
            show_frequency_filters_elements(self.ui)
            self.showCurrentImageVersion()

    # Inverse image
    def inverseCurrentImage(self):
        self.current_image_version = inverse_current_image(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # show rotate image elements
    def showRotateImageElements(self):
        show_rotate_image_elements(self.ui)
        self.showCurrentImageVersion()
    
    # rotate image
    def rotateImage(self):
        self.current_image_version = rotate_current_image(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # show resize image elements
    def showResizeImageElements(self):
        show_resize_image_elements(self.ui)
        self.showCurrentImageVersion()
    
    def resizeImagePercentage(self):
        self.current_image_version = resize_image_with_percentage(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    def resizeImageHeightWidth(self):
        self.current_image_version = resize_image_with_width_height(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # Afficher l'histogramme
    def showHistogram(self):
        show_histogram(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # Afficher l'histogramme
    def equalizeImage(self):
        self.current_image_version = equalized_image(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # Afficher l'histogramme
    def setretchImage(self):
        self.current_image_version = stretched_image(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # Afficher les elements de manual thresholding
    def showManualThresholdingElements(self):
        show_manual_thresholding(self.ui)
        self.showCurrentImageVersion()

    # Appliquer binarisation d'otsu
    def applyOtsuThresholding(self):
        self.current_image_version = apply_otsu_thresholding(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # Appliquer la binarisation manual
    def applyManualThresholding(self):
        self.current_image_version = apply_manual_thresholding(self.ui,  self.current_image_version)
        self.showCurrentImageVersion()

    # Afficher les elements de bas de filtrage gaussien
    def showGaussienFilterElements(self):
        show_gaussien_bottom_elements(self.ui)
        self.showCurrentImageVersion()

    # Afficher les elements de bas de filtrage median
    def showMedianFilterElements(self):
        show_median_bottom_elements(self.ui)
        self.showCurrentImageVersion()

    # Afficher les elements de bas de filtrage moyenne
    def showMeanFilterElements(self):
        show_mean_bottom_elements(self.ui)
        self.showCurrentImageVersion()

    # Apply mean filter
    def applyMeanFilter(self):
        self.current_image_version = apply_filter_mean(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # Apply mean filter
    def applyMedianFilter(self):
        self.current_image_version = apply_filter_median(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # Apply median filter
    def applyMedianFilter(self):
        self.current_image_version = apply_filter_median(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # Apply gaussien filter
    def applyGaussienFilter(self):
        self.current_image_version = apply_filter_gaussien(self.ui, self.current_image_version)
        self.showCurrentImageVersion()

    # Afficher les elements de filter ideale
    def showIdealFilterElements(self):
        show_ideal_bottom_elements(self.ui)
        self.showCurrentImageVersion()

    # Afficher les elements de filtre gaussien 
    def showGaussFilterElements(self):
        show_gauss_bottom_elements(self.ui)
        self.showCurrentImageVersion()

    # Afficher les elements de filtre butter worth
    def showButterWorthFilterElements(self):
        show_butterworth_bottom_elements(self.ui)
        self.showCurrentImageVersion()

    # Afficher les buttons de contours
    def showContoursElements(self):
        if self.original_image is not None:
            show_contours_elements(self.ui)
            self.showCurrentImageVersion()

    # Afficher les buttons de morphology
    def showMorphologyElements(self):
        if self.original_image is not None:
            show_morphology_elements(self.ui)
            self.showCurrentImageVersion()

    # afficher les elements de l'erosion
    def showErosionElements(self):
        show_erosion_elements(self.ui)
        self.showCurrentImageVersion()

    # afficher les elements de dilatation
    def showDilatationElements(self):
        show_dilatation_elements(self.ui)
        self.showCurrentImageVersion()

    # afficher les elements de l'erosion
    def showOuvertureElements(self):
        show_ouverture_elements(self.ui)
        self.showCurrentImageVersion()

    # afficher les elements de dilatation
    def showFermetureElements(self):
        show_fermeture_elements(self.ui)
        self.showCurrentImageVersion()

    # appliquer l'operateur sobel
    def applySobel(self):
        self.current_image_version = apply_sobel(self.current_image_version)
        self.showCurrentImageVersion()

    # appliquer l'operateur robert
    def applyRobert(self):
        self.current_image_version = apply_robert(self.current_image_version)
        self.showCurrentImageVersion()

    # appliquer l'operateur laplacien
    def applyLaplacien(self):
        self.current_image_version = apply_laplacien(self.current_image_version)
        self.showCurrentImageVersion()

    def choseEsForErosion(self):
        value = self.ui.element_structurant_taille_erosion.value()
        self.choseES("erosion", value)

    def choseEsForDilatation(self):
        value = self.ui.element_structurant_taille_dilatation.value()
        self.choseES("dilatation", value)

    def choseEsForOuverture(self):
        value = self.ui.element_structurant_taille_ouverture.value()
        self.choseES("ouverture", value)

    def choseEsForFermeture(self):
        value = self.ui.element_structurant_taille_fermeture.value()
        self.choseES("fermeture", value)

    # Choisir l'element structurant
    def choseES(self, morph, value):
        self.morph = morph
        if value % 2 == 0:
            value += 1
        self.showMatrix(value)

    # afficher la matrice de l'element structurant
    def showMatrix(self, taille):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle('Element Structurant')
        
        # Créer le layout principal vertical
        main_layout = QVBoxLayout()
        
        # Créer un layout en grille pour les cases à cocher
        grid_layout = QGridLayout()
        
        # Stocker les références des cases à cocher dans une liste de listes
        self.checkboxes = []
        
        for i in range(taille):
            row = []
            for j in range(taille):
                checkbox = QCheckBox('', self.dialog)
                checkbox.setChecked(True)
                grid_layout.addWidget(checkbox, i, j)
                row.append(checkbox)
            self.checkboxes.append(row)
        
        # Ajouter le layout en grille au layout principal
        main_layout.addLayout(grid_layout)
        
        # Ajouter le bouton OK
        ok_button = QPushButton('OK', self.dialog)
        ok_button.clicked.connect(self.getES)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        
        # Ajouter le layout du bouton au layout principal
        main_layout.addLayout(button_layout)
        
        self.dialog.setLayout(main_layout)
        self.dialog.exec_()

    # recuperer l'element structurant et application de filter morphologique
    def getES(self):
        # Créer une matrice numpy
        elementS = np.zeros((len(self.checkboxes), len(self.checkboxes[0])), dtype=int)
        for i, row in enumerate(self.checkboxes):
            for j, checkbox in enumerate(row):
                elementS[i, j] = 1 if checkbox.isChecked() else 0
        
        # Fermer la fenêtre de dialogue après avoir imprimé la matrice
        self.dialog.accept()
        print(elementS)
        if (self.morph == "erosion"):
            self.applyErosion(elementS)
        elif (self.morph == "dilatation"):
            self.applyDilatation(elementS)
        elif (self.morph == "ouverture"):
            self.applyOuverture(elementS)
        elif (self.morph == "fermeture"):
            self.applyFermeture(elementS)

    # appliquer l'erosion
    def applyErosion(self, es):
        self.current_image_version = applyErosion(self.current_image_version, es)
        self.showCurrentImageVersion()

    # appliquer dilatation
    def applyDilatation(self, es):
        self.current_image_version = applyDilatation(self.current_image_version, es)
        self.showCurrentImageVersion()

    # appliquer ouverture
    def applyOuverture(self, es):
        self.current_image_version = applyOuverture(self.current_image_version, es)
        self.showCurrentImageVersion()

    # appliquer fermeture
    def applyFermeture(self, es):
        self.current_image_version = applyFermeture(self.current_image_version, es)
        self.showCurrentImageVersion()

    def applyBasIdealFilter(self):
        seuil = self.ui.seuil_passe_bas_ideal_filter.value()
        print(seuil)
        self.current_image_version = applyBasIdealFilter(self.current_image_version, seuil)
        self.showCurrentImageVersion()

    def applyHautIdealFilter(self):
        seuil = self.ui.seuil_passe_haut_ideal_filter.value()
        self.current_image_version = applyHautIdealFilter(self.current_image_version, seuil)
        self.showCurrentImageVersion()

    def applyBasGaussienFilter(self):
        seuil = self.ui.seuil_passe_bas_gaussien_filter.value()
        self.current_image_version = applyBasGaussienFilter(self.current_image_version, seuil)
        self.showCurrentImageVersion()
        print(seuil)

    def applyHautGaussienFilter(self):
        seuil = self.ui.seuil_passe_haut_gaussien_filter.value()
        self.current_image_version = applyHautGaussienFilter(self.current_image_version, seuil)
        self.showCurrentImageVersion()
        print(seuil)

    def applyBasButterworthFilter(self):
        seuil = self.ui.seuil_passe_bas_butterworth_filter.value()
        order = self.ui.order_passe_bas_butterworth_filter.value()
        self.current_image_version = applyBasButterWorthFilter(self.current_image_version, seuil, order)
        self.showCurrentImageVersion()

    def applyHautButterworthFilter(self):
        seuil = self.ui.seuil_passe_haut_butterworth_filter.value()
        order = self.ui.order_passe_haut_butterworth_filter.value()
        self.current_image_version = applyHautButterWorthFilter(self.current_image_version, seuil, order)
        self.showCurrentImageVersion()

    # afficher huffman elements
    def showHuffmanElements(self):
        showHuffmanElements(self.ui)
        self.showCurrentImageVersion()

    # appliquer huffman
    def applyHuffman(self):
        file_name = self.ui.huffman_file_name.text()
        applyHuffman(self.current_image_version, file_name)

    # afficher les elements de hough
    def showHoughElements(self):
        showHoughElements(self.ui)
        self.showCurrentImageVersion()

    # appliquer hough
    def applyHough(self):
        seuil = self.ui.threshold.value()
        self.current_image_version = applyHough(self.current_image_version, seuil)
        self.showCurrentImageVersion()

    # afficher les elements de kmeans
    def showKmeansElements(self):
        show_kmeans_elements(self.ui)
        self.showCurrentImageVersion()

    # apply kmeans
    def applyKmeans(self):
        k = self.ui.k.value()
        self.current_image_version = applyKmeans(self.current_image_version, k)
        self.showCurrentImageVersion()

    # enregistrer l'image
    def save_image(self):
        if self.current_image_version is not None:
            save_file_dialog(self.ui, self.current_image_version)

    # afficher les methodes de segmentation
    def showSegmentationElements(self):
        if self.current_image_version is not None:
            show_segmentation_elements(self.ui)
            self.showCurrentImageVersion()

    # afficher les methodes de compression
    def showCompressionElements(self):
        if self.current_image_version is not None:
            show_compression_elements(self.ui)
            self.showCurrentImageVersion()

    # afficher les methodes d'extraction des points d'interet
    def showPointsOfInterestElements(self):
        if self.current_image_version is not None:
            show_points_of_interest_elements(self.ui)
            self.showCurrentImageVersion()

# starting executing processus from here
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())