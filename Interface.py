from PyQt5 import QtCore, QtGui, QtWidgets # type: ignore
from PyQt5.QtWidgets import QLineEdit # type: ignore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Fenetre principale 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 604)
        MainWindow.setStyleSheet("")

        self.main_window = QtWidgets.QWidget(MainWindow)
        self.main_window.setStyleSheet("")
        self.main_window.setObjectName("main_window")

        # Layout horizontal de la fenetre principale ( 3 parties dedans )
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_window)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #=================================================#
        #                 partie de gauche                #
        #=================================================#

        self.left_menu = QtWidgets.QWidget(self.main_window)
        self.left_menu.setStyleSheet("""
                                        #left_menu {
                                            background-color: #496989;
                                            max-width: 160px;
                                        }
                                    """)
        self.left_menu.setObjectName("left_menu")

        # Layout verticale ( 3 parties dedans )
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left_menu)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Partie de haut de la partie de gauche de fenetre principale
        self.left_menu_top_part = QtWidgets.QWidget(self.left_menu)
        self.left_menu_top_part.setStyleSheet("""
                                                #left_menu_top_part {
                                                    max-height: 100px;
                                                }
                                            """)

        self.left_menu_top_part.setObjectName("left_menu_top_part")
        self.verticalLayout.addWidget(self.left_menu_top_part)
        
        # Partie de centre de la partie de gauche de fenetre principale ( contient les bottons )
        self.left_menu_center_part = QtWidgets.QWidget(self.left_menu)
        self.left_menu_center_part.setStyleSheet("")
        self.left_menu_center_part.setObjectName("left_menu_center_part")

        # Son layout vertical
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_menu_center_part)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        #=================================================#
        #                    Les bottons                  #
        #=================================================#

        self.left_menu_base_actions = QtWidgets.QLabel(self.left_menu_center_part)
        self.left_menu_base_actions.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_base_actions.setObjectName("left_menu_base_actions")
        self.verticalLayout_2.addWidget(self.left_menu_base_actions)

        self.left_menu_binarization = QtWidgets.QLabel(self.left_menu_center_part)
        self.left_menu_binarization.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_binarization.setObjectName("left_menu_binarization")
        self.verticalLayout_2.addWidget(self.left_menu_binarization)

        self.left_menu_filters = QtWidgets.QLabel(self.left_menu_center_part)
        self.left_menu_filters.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_filters.setObjectName("left_menu_filters")
        self.verticalLayout_2.addWidget(self.left_menu_filters)

        self.left_menu_frequency_feltring = QtWidgets.QLabel(self.left_menu_center_part)
        self.left_menu_frequency_feltring.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_frequency_feltring.setObjectName("left_menu_frequency_feltring")
        self.verticalLayout_2.addWidget(self.left_menu_frequency_feltring)

        self.left_menu_contours = QtWidgets.QLabel(self.left_menu_center_part)
        self.left_menu_contours.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_contours.setObjectName("left_menu_contours")
        self.verticalLayout_2.addWidget(self.left_menu_contours)

        self.left_menu_morphology = QtWidgets.QLabel(self.left_menu_center_part)
        self.left_menu_morphology.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_morphology.setObjectName("left_menu_morphology")
        self.verticalLayout_2.addWidget(self.left_menu_morphology)

        self.left_menu_segmentation = QtWidgets.QLabel(self.left_menu_center_part)
        self.left_menu_segmentation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_segmentation.setObjectName("left_menu_segmentation")
        self.verticalLayout_2.addWidget(self.left_menu_segmentation)

        self.left_menu_points_of_interest = QtWidgets.QLabel(self.left_menu_center_part)
        self.left_menu_points_of_interest.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_points_of_interest.setObjectName("left_menu_points_of_interest")
        self.verticalLayout_2.addWidget(self.left_menu_points_of_interest)

        self.left_menu_compression = QtWidgets.QLabel(self.left_menu_center_part)
        self.left_menu_compression.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_compression.setObjectName("left_menu_compression")
        self.verticalLayout_2.addWidget(self.left_menu_compression)

        # Ajouter le menu de gauche ( partie de centre de gauche ) au layout vertical de partie gauche
        self.verticalLayout.addWidget(self.left_menu_center_part)
        
        # Partie de bas de la partie de gauche de fenetre principale
        self.left_menu_bottom_part = QtWidgets.QWidget(self.left_menu)
        self.left_menu_bottom_part.setStyleSheet("""
                                                    #left_menu_bottom_part {
                                                        max-height: 100px;
                                                    }
                                                """)
        self.left_menu_bottom_part.setObjectName("left_menu_bottom_part")

        # Son layout
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_menu_bottom_part)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        # Contenu de cette partie de bas
        self.line = QtWidgets.QFrame(self.left_menu_bottom_part)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        
        self.left_menu_save_image = QtWidgets.QLabel(self.left_menu_bottom_part)
        self.left_menu_save_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_save_image.setObjectName("left_menu_save_image")
        self.verticalLayout_3.addWidget(self.left_menu_save_image)
        
        # Ajouter cette partie au layout verticale de partie gauche
        self.verticalLayout.addWidget(self.left_menu_bottom_part)
        
        # Ajouter la partie de gauche à notre layout horizantal de fenetre principale
        self.horizontalLayout.addWidget(self.left_menu)
        
        #=================================================#
        #                 Partie de centre                #
        #=================================================#

        self.main_body = QtWidgets.QWidget(self.main_window)
        self.main_body.setStyleSheet("""
                                        #main_body {
                                            background-color: #F6F1EE;
                                        }
                                    """)
        self.main_body.setObjectName("main_body")

        # Layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        #=================================================#
        #              buttons base actions               #
        #=================================================#

        self.main_body_top_part_base_actions = QtWidgets.QWidget(self.main_body)
        self.main_body_top_part_base_actions.setStyleSheet("""
                                                            #main_body_top_part_base_actions {
                                                                max-height: 50px;
                                                                background-color: #E2F4C5;
                                                            }
                                                        """)
        self.main_body_top_part_base_actions.setObjectName("main_body_top_part_base_actions")
        
        self.inverse_image = QtWidgets.QLabel(self.main_body_top_part_base_actions)
        self.inverse_image.setGeometry(QtCore.QRect(60, 10, 121, 31))
        self.inverse_image.setObjectName("inverse_image")
        
        self.rotate_image = QtWidgets.QLabel(self.main_body_top_part_base_actions)
        self.rotate_image.setGeometry(QtCore.QRect(200, 10, 121, 31))
        self.rotate_image.setObjectName("rotate_image")
        
        self.resize_image = QtWidgets.QLabel(self.main_body_top_part_base_actions)
        self.resize_image.setGeometry(QtCore.QRect(340, 10, 111, 31))
        self.resize_image.setObjectName("resize_image")
        
        self.histogramme = QtWidgets.QLabel(self.main_body_top_part_base_actions)
        self.histogramme.setGeometry(QtCore.QRect(470, 10, 111, 31))
        self.histogramme.setObjectName("histogramme")
        
        self.equalize = QtWidgets.QLabel(self.main_body_top_part_base_actions)
        self.equalize.setGeometry(QtCore.QRect(600, 10, 81, 31))
        self.equalize.setObjectName("equalize")
        
        self.stretch = QtWidgets.QLabel(self.main_body_top_part_base_actions)
        self.stretch.setGeometry(QtCore.QRect(700, 10, 81, 31))
        self.stretch.setObjectName("stretch")

        # Ajouter la partie de base actions buttons au layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_top_part_base_actions)
        
        #=================================================#
        #               buttons binarization              #  
        #=================================================#

        self.main_body_top_part_binarization = QtWidgets.QWidget(self.main_body)
        self.main_body_top_part_binarization.setStyleSheet("""
                                                            #main_body_top_part_binarization {
                                                                max-height: 50px;
                                                                background-color: #E2F4C5;
                                                            }
                                                        """)
        self.main_body_top_part_binarization.setObjectName("main_body_top_part_binarization")
        
        self.manual_thresholding = QtWidgets.QLabel(self.main_body_top_part_binarization)
        self.manual_thresholding.setGeometry(QtCore.QRect(60, 10, 141, 31))
        self.manual_thresholding.setObjectName("manual_thresholding")
        
        self.otsu_thresholding = QtWidgets.QLabel(self.main_body_top_part_binarization)
        self.otsu_thresholding.setGeometry(QtCore.QRect(220, 10, 131, 31))
        self.otsu_thresholding.setObjectName("otsu_thresholding")
        
        # Ajouter la partie de binarization buttons au layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_top_part_binarization)
        
        #=================================================#
        #                buttons filters                  #
        #=================================================#

        self.main_body_top_part_filters = QtWidgets.QWidget(self.main_body)
        self.main_body_top_part_filters.setStyleSheet("""
                                                        #main_body_top_part_filters {
                                                            max-height: 50px;
                                                            background-color: #E2F4C5;
                                                        }
                                                    """)
        self.main_body_top_part_filters.setObjectName("main_body_top_part_filters")
        
        self.gaussien = QtWidgets.QLabel(self.main_body_top_part_filters)
        self.gaussien.setGeometry(QtCore.QRect(60, 10, 91, 31))
        self.gaussien.setObjectName("gaussien")

        self.mean = QtWidgets.QLabel(self.main_body_top_part_filters)
        self.mean.setGeometry(QtCore.QRect(170, 10, 71, 31))
        self.mean.setObjectName("mean")
        
        self.median = QtWidgets.QLabel(self.main_body_top_part_filters)
        self.median.setGeometry(QtCore.QRect(260, 10, 80, 31))
        self.median.setObjectName("median")
        
        # Ajouter la partie de filters buttons au layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_top_part_filters)

        #=================================================#
        #           buttons frequency feltring            #
        #=================================================#
        
        self.main_body_top_part_frequency_filters = QtWidgets.QWidget(self.main_body)
        self.main_body_top_part_frequency_filters.setStyleSheet("""
                                                                #main_body_top_part_frequency_filters {
                                                                    max-height: 50px;
                                                                    background-color: #E2F4C5;
                                                                }
                                                            """)
        self.main_body_top_part_frequency_filters.setObjectName("main_body_top_part_frequency_filters")
        
        self.ideal = QtWidgets.QLabel(self.main_body_top_part_frequency_filters)
        self.ideal.setGeometry(QtCore.QRect(60, 10, 70, 31))
        self.ideal.setObjectName("ideal")

        self.butterworth = QtWidgets.QLabel(self.main_body_top_part_frequency_filters)
        self.butterworth.setGeometry(QtCore.QRect(150, 10, 110, 31))
        self.butterworth.setObjectName("butterworth")
        
        self.gauss = QtWidgets.QLabel(self.main_body_top_part_frequency_filters)
        self.gauss.setGeometry(QtCore.QRect(280, 10, 100, 31))
        self.gauss.setObjectName("gauss")
        
        # Ajouter la partie de buttons frequency feltring au layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_top_part_frequency_filters)

        #=================================================#
        #                buttons contours                 #
        #=================================================#

        self.main_body_top_part_contours = QtWidgets.QWidget(self.main_body)
        self.main_body_top_part_contours.setStyleSheet("""
                                                            #main_body_top_part_contours {
                                                                max-height: 50px;
                                                                background-color: #E2F4C5;
                                                            }
                                                        """)
        self.main_body_top_part_contours.setObjectName("main_body_top_part_contours")
        
        self.sobel = QtWidgets.QLabel(self.main_body_top_part_contours)
        self.sobel.setGeometry(QtCore.QRect(60, 10, 80, 31))
        self.sobel.setObjectName("sobel")
        
        self.robert = QtWidgets.QLabel(self.main_body_top_part_contours)
        self.robert.setGeometry(QtCore.QRect(150, 10, 85, 31))
        self.robert.setObjectName("robert")
        
        self.laplacien = QtWidgets.QLabel(self.main_body_top_part_contours)
        self.laplacien.setGeometry(QtCore.QRect(250, 10, 90, 31))
        self.laplacien.setObjectName("laplacien")
        
        self.gradiant = QtWidgets.QLabel(self.main_body_top_part_contours)
        self.gradiant.setGeometry(QtCore.QRect(360, 10, 90, 31))
        self.gradiant.setObjectName("gradiant")
            
        # Ajouter la partie de contours buttons au layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_top_part_contours)

        #=================================================#
        #               buttons morphology                #
        #=================================================#
        self.main_body_top_part_morphology = QtWidgets.QWidget(self.main_body)
        self.main_body_top_part_morphology.setStyleSheet("""
                                                            #main_body_top_part_morphology {
                                                                max-height: 50px;
                                                                background-color: #E2F4C5;
                                                            }
                                                        """)
        self.main_body_top_part_morphology.setObjectName("main_body_top_part_morphology")
        
        self.erosion = QtWidgets.QLabel(self.main_body_top_part_morphology)
        self.erosion.setGeometry(QtCore.QRect(60, 10, 80, 31))
        self.erosion.setObjectName("erosion")
        
        self.dilatation = QtWidgets.QLabel(self.main_body_top_part_morphology)
        self.dilatation.setGeometry(QtCore.QRect(150, 10, 90, 31))
        self.dilatation.setObjectName("dilatation")
        
        self.ouverture = QtWidgets.QLabel(self.main_body_top_part_morphology)
        self.ouverture.setGeometry(QtCore.QRect(250, 10, 100, 31))
        self.ouverture.setObjectName("ouverture")
        
        self.fermeture = QtWidgets.QLabel(self.main_body_top_part_morphology)
        self.fermeture.setGeometry(QtCore.QRect(370, 10, 100, 31))
        self.fermeture.setObjectName("fermeture")
            
        # Ajouter la partie de morphologies buttons au layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_top_part_morphology)

        #=================================================#
        #              buttons segmentation               #
        #=================================================#

        self.main_body_top_part_segmentation = QtWidgets.QWidget(self.main_body)
        self.main_body_top_part_segmentation.setStyleSheet("""
                                                            #main_body_top_part_segmentation {
                                                                max-height: 50px;
                                                                background-color: #E2F4C5;
                                                            }
                                                        """)
        self.main_body_top_part_segmentation.setObjectName("main_body_top_part_segmentation")
        
        self.kmeans = QtWidgets.QLabel(self.main_body_top_part_segmentation)
        self.kmeans.setGeometry(QtCore.QRect(60, 10, 95, 31))
        self.kmeans.setObjectName("kmeans")
        
        self.region_croissance = QtWidgets.QLabel(self.main_body_top_part_segmentation)
        self.region_croissance.setGeometry(QtCore.QRect(170, 10, 140, 31))
        self.region_croissance.setObjectName("region_croissance")
        
        self.regions_partition = QtWidgets.QLabel(self.main_body_top_part_segmentation)
        self.regions_partition.setGeometry(QtCore.QRect(320, 10, 140, 31))
        self.regions_partition.setObjectName("regions_partition")

        # Ajouter la partie de segmentations buttons au layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_top_part_segmentation)

        #=================================================#
        #           buttons points of interest            #
        #=================================================#

        self.main_body_top_part_points_of_interest = QtWidgets.QWidget(self.main_body)
        self.main_body_top_part_points_of_interest.setStyleSheet("""
                                                            #main_body_top_part_points_of_interest {
                                                                max-height: 50px;
                                                                background-color: #E2F4C5;
                                                            }
                                                        """)
        self.main_body_top_part_points_of_interest.setObjectName("main_body_top_part_points_of_interest")
        
        self.hough = QtWidgets.QLabel(self.main_body_top_part_points_of_interest)
        self.hough.setGeometry(QtCore.QRect(60, 10, 80, 31))
        self.hough.setObjectName("hough")

        # Ajouter la partie de points d'interet buttons au layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_top_part_points_of_interest)

        #=================================================#
        #           buttons points compression            #
        #=================================================#

        self.main_body_top_part_compression = QtWidgets.QWidget(self.main_body)
        self.main_body_top_part_compression.setStyleSheet("""
                                                            #main_body_top_part_compression {
                                                                max-height: 50px;
                                                                background-color: #E2F4C5;
                                                            }
                                                        """)
        self.main_body_top_part_compression.setObjectName("main_body_top_part_compression")
        
        self.huffman = QtWidgets.QLabel(self.main_body_top_part_compression)
        self.huffman.setGeometry(QtCore.QRect(60, 10, 85, 31))
        self.huffman.setObjectName("huffman")

        self.lzw = QtWidgets.QLabel(self.main_body_top_part_compression)
        self.lzw.setGeometry(QtCore.QRect(160, 10, 70, 31))
        self.lzw.setObjectName("lzw")

        # Ajouter la partie de points d'interet buttons au layout vertical de la partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_top_part_compression)

        #=================================================#
        #    partie de ce centre de la partie de centre   #
        #    de la fenetre principale                     #
        #=================================================#

        self.main_body_center_part = QtWidgets.QWidget(self.main_body)
        self.main_body_center_part.setObjectName("main_body_center_part")

        # image place
        self.image_place = QtWidgets.QLabel(self.main_body_center_part)
        self.image_place.setText("")
        self.image_place.setScaledContents(True)
        self.image_place.setObjectName("image_place")
        self.image_place.hide()

        # Ajouter cette partie au partie de centre de partie de centre de fenetre principale
        self.verticalLayout_4.addWidget(self.main_body_center_part)
        
        # Ajouter la partie de centre au fenetre principale
        self.horizontalLayout.addWidget(self.main_body)

        #=================================================#
        #     La partie de droite de fenetre principale   #
        #=================================================#

        self.right_menu = QtWidgets.QWidget(self.main_window)
        self.right_menu.setStyleSheet("""
                                        #right_menu {
                                            background-color: #496989;
                                            max-width: 100px;
                                        }
                                    """)
        self.right_menu.setObjectName("right_menu")

        # Contenu de cette partie
        self.image_original = QtWidgets.QLabel(self.right_menu)
        self.image_original.setGeometry(QtCore.QRect(10, 180, 81, 31))
        self.image_original.setObjectName("image_original")

        self.image_current = QtWidgets.QLabel(self.right_menu)
        self.image_current.setGeometry(QtCore.QRect(10, 230, 81, 31))
        self.image_current.setObjectName("image_current")

        self.image_orig = QtWidgets.QLabel(self.right_menu)
        self.image_orig.setGeometry(QtCore.QRect(10, 280, 81, 31))
        self.image_orig.setObjectName("image_orig")
        self.image_orig.setStyleSheet("""
                        #image_orig {
                            color: white;   
                            font-size: 12px;
                            padding-left: 9%;    
                            padding-top: 2px;
                            padding-bottom: 2px;}
                        #image_orig:hover {
                                color: black;  background-color: white;}
                                                    """)

        # Son layout
        self.horizontalLayout.addWidget(self.right_menu)
        
        # Ajouter le widget main_window comme le widget central de la fenetre principale
        MainWindow.setCentralWidget(self.main_window)
        
        # btn load image ajouté à la partie de centre de fenetre principale
        self.load_image = QtWidgets.QPushButton(self.main_body)
        self.load_image.setGeometry(QtCore.QRect(410, 310, 171, 31))
        self.load_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.load_image.setObjectName("load_image")
        
        #=================================================#
        #        La partie de bas de rotate immage        #
        #=================================================#

        self.main_body_bottom_part_rotate_image = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_rotate_image.setStyleSheet("""
                                                            #main_body_bottom_part_rotate_image {
                                                                background-color: #C5FF95;
                                                                max-height: 50px;
                                                            }
                                                        """)
        self.main_body_bottom_part_rotate_image.setObjectName("main_body_bottom_part_rotate_image")

        # contenu de cette partie
        self.label_rotation_angle = QtWidgets.QLabel(self.main_body_bottom_part_rotate_image)
        self.label_rotation_angle.setGeometry(QtCore.QRect(270, 20, 71, 16))
        self.label_rotation_angle.setStyleSheet("#label_rotation_angle {\n"
                                                                        "height: 30px;\n"
                                                                        "}")
        self.label_rotation_angle.setObjectName("label_rotation_angle")
        
        self.button_rotate = QtWidgets.QPushButton(self.main_body_bottom_part_rotate_image)
        self.button_rotate.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.button_rotate.setObjectName("button_rotate")
        
        self.rotation_angle = QtWidgets.QSpinBox(self.main_body_bottom_part_rotate_image)
        self.rotation_angle.setGeometry(QtCore.QRect(350, 10, 42, 31))
        self.rotation_angle.setObjectName("rotation_angle")
        self.rotation_angle.setMinimum(0)
        self.rotation_angle.setMaximum(360)
        self.rotation_angle.setValue(45)

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_rotate_image)
        
        #=================================================#
        #       La partie de bas de resize image          #
        #=================================================#
        
        self.main_body_bottom_part_resize_image = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_resize_image.setStyleSheet("#main_body_bottom_part_resize_image {\n"
                                                                                "background-color: #C5FF95;\n"
                                                                                "max-height: 50px;\n"
                                                                                "}")
        self.main_body_bottom_part_resize_image.setObjectName("main_body_bottom_part_resize_image")
        
        # contenu de cette partie
        self.label_pecentage = QtWidgets.QLabel(self.main_body_bottom_part_resize_image)
        self.label_pecentage.setGeometry(QtCore.QRect(80, 20, 61, 16))
        self.label_pecentage.setStyleSheet("")
        self.label_pecentage.setObjectName("label_pecentage")
        
        self.button_percentage = QtWidgets.QPushButton(self.main_body_bottom_part_resize_image)
        self.button_percentage.setGeometry(QtCore.QRect(270, 10, 75, 31))
        self.button_percentage.setObjectName("button_percentage")
        
        self.percentage = QtWidgets.QSpinBox(self.main_body_bottom_part_resize_image)
        self.percentage.setMaximum(2000)
        self.percentage.setValue(100)
        self.percentage.setGeometry(QtCore.QRect(140, 10, 42, 31))
        self.percentage.setObjectName("percentage")
        
        self.line_2 = QtWidgets.QFrame(self.main_body_bottom_part_resize_image)
        self.line_2.setGeometry(QtCore.QRect(380, 0, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.width = QtWidgets.QSpinBox(self.main_body_bottom_part_resize_image)
        self.width.setMaximum(2000)
        self.width.setGeometry(QtCore.QRect(490, 10, 42, 31))
        self.width.setObjectName("width")
        
        self.label_width = QtWidgets.QLabel(self.main_body_bottom_part_resize_image)
        self.label_width.setGeometry(QtCore.QRect(450, 20, 31, 16))
        self.label_width.setStyleSheet("")
        self.label_width.setObjectName("label_width")
        
        self.label_height = QtWidgets.QLabel(self.main_body_bottom_part_resize_image)
        self.label_height.setGeometry(QtCore.QRect(550, 20, 31, 16))
        self.label_height.setStyleSheet("")
        self.label_height.setObjectName("label_height")
        
        self.height = QtWidgets.QSpinBox(self.main_body_bottom_part_resize_image)
        self.height.setMaximum(2000)
        self.height.setGeometry(QtCore.QRect(590, 10, 42, 31))
        self.height.setObjectName("height")
        
        self.button_width_height = QtWidgets.QPushButton(self.main_body_bottom_part_resize_image)
        self.button_width_height.setGeometry(QtCore.QRect(730, 10, 75, 31))
        self.button_width_height.setObjectName("button_width_height")
        
        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_resize_image)

        #=================================================#
        #       La partie de bas de otsu bottom menu      #
        #=================================================#

        self.main_body_bottom_part_otsu_threshold = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_otsu_threshold.setStyleSheet("""
                                                                    #main_body_bottom_part_otsu_threshold {
                                                                        background-color: #C5FF95;
                                                                        max-height: 50px;
                                                                    }
                                                                """)
        self.main_body_bottom_part_otsu_threshold.setObjectName("main_body_bottom_part_otsu_threshold")
        
        # contenu de cette partie
        self.otsu_threshold = QtWidgets.QLabel(self.main_body_bottom_part_otsu_threshold)
        self.otsu_threshold.setGeometry(QtCore.QRect(380, 20, 81, 16))
        self.otsu_threshold.setObjectName("otsu_threshold")
        
        self.otsu_threshold_value = QtWidgets.QLabel(self.main_body_bottom_part_otsu_threshold)
        self.otsu_threshold_value.setGeometry(QtCore.QRect(480, 20, 47, 16))
        self.otsu_threshold_value.setObjectName("otsu_threshold_value")
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_otsu_threshold)
        
        self.main_body_bottom_part_manual_threshold = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_manual_threshold.setStyleSheet("#main_body_bottom_part_manual_threshold {\n"
                                                                    "    background-color: #C5FF95;\n"
                                                                    "    max-height: 50px;\n"
                                                                    "}")
        self.main_body_bottom_part_manual_threshold.setObjectName("main_body_bottom_part_manual_threshold")
        
        self.label_otsu_manual_threshold = QtWidgets.QLabel(self.main_body_bottom_part_manual_threshold)
        self.label_otsu_manual_threshold.setGeometry(QtCore.QRect(310, 20, 81, 16))
        self.label_otsu_manual_threshold.setObjectName("label_otsu_manual_threshold")
        
        self.otsu_manual_threshold = QtWidgets.QSpinBox(self.main_body_bottom_part_manual_threshold)
        self.otsu_manual_threshold.setMaximum(255)
        self.otsu_manual_threshold.setGeometry(QtCore.QRect(390, 10, 42, 31))
        self.otsu_manual_threshold.setObjectName("otsu_manual_threshold")
        
        self.button_threshold = QtWidgets.QPushButton(self.main_body_bottom_part_manual_threshold)
        self.button_threshold.setGeometry(QtCore.QRect(531, 10, 75, 31))
        self.button_threshold.setObjectName("button_threshold")
        
        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_manual_threshold)
        
        #=================================================#
        #    La partie de bas de mean filter bottom part  #
        #=================================================#

        self.main_body_bottom_part_mean = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_mean.setStyleSheet("#main_body_bottom_part_mean {\n"
                                                                        "background-color: #C5FF95;\n"
                                                                        "max-height: 50px;\n"
                                                                        "}")
        self.main_body_bottom_part_mean.setObjectName("main_body_bottom_part_mean")

        # contenu de cette partie
        self.label_taille_filter_mean = QtWidgets.QLabel(self.main_body_bottom_part_mean)
        self.label_taille_filter_mean.setGeometry(QtCore.QRect(295, 17, 71, 16))
        self.label_taille_filter_mean.setStyleSheet("#label_taille_filter_mean {\n"
                                                                        "height: 30px;\n"
                                                                        "}")
        self.label_taille_filter_mean.setObjectName("label_taille_filter_mean")

        self.button_apply_mean_filter = QtWidgets.QPushButton(self.main_body_bottom_part_mean)
        self.button_apply_mean_filter.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.button_apply_mean_filter.setObjectName("button_apply_mean_filter")

        self.taille_mean_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_mean)
        self.taille_mean_filter.setGeometry(QtCore.QRect(350, 10, 42, 31))
        self.taille_mean_filter.setObjectName("taille mean filter")
        self.taille_mean_filter.setMinimum(0)
        self.taille_mean_filter.setMaximum(50)
        self.taille_mean_filter.setValue(3)
        
        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_mean)        
        
        #=================================================#
        #      La partie de bas de median bottom part     #
        #=================================================#

        self.main_body_bottom_part_median = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_median.setStyleSheet("#main_body_bottom_part_median {\n"
                                                                        "background-color: #C5FF95;\n"
                                                                        "max-height: 50px;\n"
                                                                        "}")
        self.main_body_bottom_part_median.setObjectName("main_body_bottom_part_median")

        # Contenu de cette partie
        self.label_taille_filter_median = QtWidgets.QLabel(self.main_body_bottom_part_median)
        self.label_taille_filter_median.setGeometry(QtCore.QRect(295, 17, 71, 16))
        self.label_taille_filter_median.setStyleSheet("#label_taille_filter_median {\n"
                                                                        "height: 30px;\n"
                                                                        "}")
        self.label_taille_filter_median.setObjectName("label_taille_filter_median")

        self.button_apply_median_filter = QtWidgets.QPushButton(self.main_body_bottom_part_median)
        self.button_apply_median_filter.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.button_apply_median_filter.setObjectName("button_apply_median_filter")

        self.taille_median_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_median)
        self.taille_median_filter.setGeometry(QtCore.QRect(350, 10, 42, 31))
        self.taille_median_filter.setObjectName("taille mean filter")
        self.taille_median_filter.setMinimum(0)
        self.taille_median_filter.setMaximum(50)
        self.taille_median_filter.setValue(3)

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_median)

        #=================================================#
        #     La partie de bas de gaussien bottom part    #
        #=================================================#

        self.main_body_bottom_part_gaussien = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_gaussien.setStyleSheet("#main_body_bottom_part_gaussien {\n"
                                                                        "background-color: #C5FF95;\n"
                                                                        "max-height: 50px;\n"
                                                                        "}")
        self.main_body_bottom_part_gaussien.setObjectName("main_body_bottom_part_gaussien")

        # Contenu de cette partie
        self.label_ecartType_gaussien_filter = QtWidgets.QLabel(self.main_body_bottom_part_gaussien)
        self.label_ecartType_gaussien_filter.setGeometry(QtCore.QRect(185, 17, 71, 16))
        self.label_ecartType_gaussien_filter.setStyleSheet("#label_ecartType_gaussien_filter {\n"
                                                                        "height: 30px;\n"
                                                                        "}")
        self.label_ecartType_gaussien_filter.setObjectName("label_ecartType_gaussien_filter")

        self.ecartType_gaussien_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_gaussien)
        self.ecartType_gaussien_filter.setGeometry(QtCore.QRect(250, 10, 42, 31))
        self.ecartType_gaussien_filter.setObjectName("ecartType_gaussien_filter")
        self.ecartType_gaussien_filter.setMinimum(0)
        self.ecartType_gaussien_filter.setMaximum(20)
        self.ecartType_gaussien_filter.setValue(1)

        self.label_taille_filter_gaussien = QtWidgets.QLabel(self.main_body_bottom_part_gaussien)
        self.label_taille_filter_gaussien.setGeometry(QtCore.QRect(382, 17, 71, 16))
        self.label_taille_filter_gaussien.setStyleSheet("#label_taille_filter_gaussien {\n"
                                                                        "height: 30px;\n"
                                                                        "}")
        self.label_taille_filter_gaussien.setObjectName("label_taille_filter_gaussien")

        self.taille_gaussien_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_gaussien)
        self.taille_gaussien_filter.setGeometry(QtCore.QRect(435, 10, 42, 31))
        self.taille_gaussien_filter.setObjectName("taille gaussien filter")
        self.taille_gaussien_filter.setMinimum(0)
        self.taille_gaussien_filter.setMaximum(50)
        self.taille_gaussien_filter.setValue(3)

        self.button_apply_gaussien_filter = QtWidgets.QPushButton(self.main_body_bottom_part_gaussien)
        self.button_apply_gaussien_filter.setGeometry(QtCore.QRect(595, 10, 75, 31))
        self.button_apply_gaussien_filter.setObjectName("button_apply_gaussien_filter")

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_gaussien)

        # ================================================= #
        #           Partie de bas de filtre ideal           #
        # ================================================= #
        self.main_body_bottom_part_frequency_filtring_ideal = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_frequency_filtring_ideal.setStyleSheet("#main_body_bottom_part_frequency_filtring_ideal {\n"
                                                                            "    background-color: #C5FF95;\n"
                                                                            "    max-height: 50px;\n"
                                                                            "}")
        self.main_body_bottom_part_frequency_filtring_ideal.setObjectName("main_body_bottom_part_frequency_filtring_ideal")

        # Contenu de cette partie
        self.line_2 = QtWidgets.QFrame(self.main_body_bottom_part_frequency_filtring_ideal)
        self.line_2.setGeometry(QtCore.QRect(430, 0, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_passe_bas = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_ideal)
        self.label_passe_bas.setGeometry(QtCore.QRect(40, 16, 61, 20))
        self.label_passe_bas.setObjectName("label_passe_bas")

        self.label_passe_haut = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_ideal)
        self.label_passe_haut.setGeometry(QtCore.QRect(460, 15, 61, 21))
        self.label_passe_haut.setObjectName("label_passe_haut")

        self.apply_passe_bas_ideal_filter = QtWidgets.QPushButton(self.main_body_bottom_part_frequency_filtring_ideal)
        self.apply_passe_bas_ideal_filter.setGeometry(QtCore.QRect(330, 10, 75, 31))
        self.apply_passe_bas_ideal_filter.setObjectName("apply_passe_bas_ideal_filter")

        self.apply_passe_haut_ideal_filter = QtWidgets.QPushButton(self.main_body_bottom_part_frequency_filtring_ideal)
        self.apply_passe_haut_ideal_filter.setGeometry(QtCore.QRect(740, 10, 75, 31))
        self.apply_passe_haut_ideal_filter.setObjectName("apply_passe_haut_ideal_filter")

        self.seuil_passe_haut_ideal_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_frequency_filtring_ideal)
        self.seuil_passe_haut_ideal_filter.setGeometry(QtCore.QRect(680, 10, 42, 31))
        self.seuil_passe_haut_ideal_filter.setMinimum(1)
        self.seuil_passe_haut_ideal_filter.setMaximum(50)
        self.seuil_passe_haut_ideal_filter.setObjectName("seuil_passe_haut_ideal_filter")

        self.seuil_passe_bas_ideal_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_frequency_filtring_ideal)
        self.seuil_passe_bas_ideal_filter.setGeometry(QtCore.QRect(270, 10, 42, 31))
        self.seuil_passe_bas_ideal_filter.setMinimum(1)
        self.seuil_passe_bas_ideal_filter.setMaximum(50)
        self.seuil_passe_bas_ideal_filter.setObjectName("seuil_passe_bas_ideal_filter")

        self.label_seuil_passe_bas = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_ideal)
        self.label_seuil_passe_bas.setGeometry(QtCore.QRect(230, 20, 47, 13))
        self.label_seuil_passe_bas.setObjectName("label_seuil_passe_bas")

        self.label_seuil_passe_haut = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_ideal)
        self.label_seuil_passe_haut.setGeometry(QtCore.QRect(640, 20, 47, 13))
        self.label_seuil_passe_haut.setObjectName("label_seuil_passe_haut")

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_frequency_filtring_ideal)

        # ================================================= #
        #        Partie de bas de filtre butterworth        #
        # ================================================= #
        self.main_body_bottom_part_frequency_filtring_butterworth = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_frequency_filtring_butterworth.setStyleSheet("#main_body_bottom_part_frequency_filtring_butterworth {\n"
                                                                            "    background-color: #C5FF95;\n"
                                                                            "    max-height: 50px;\n"
                                                                            "}")
        self.main_body_bottom_part_frequency_filtring_butterworth.setObjectName("main_body_bottom_part_frequency_filtring_butterworth")
        
        # Contenu de cette partie
        self.line_4 = QtWidgets.QFrame(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.line_4.setGeometry(QtCore.QRect(430, 0, 3, 61))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.label_passe_bas_2 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.label_passe_bas_2.setGeometry(QtCore.QRect(40, 16, 61, 20))
        self.label_passe_bas_2.setObjectName("label_passe_bas_2")

        self.label_passe_haut_2 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.label_passe_haut_2.setGeometry(QtCore.QRect(460, 15, 61, 21))
        self.label_passe_haut_2.setObjectName("label_passe_haut_2")

        self.apply_passe_bas_butterworth_filter = QtWidgets.QPushButton(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.apply_passe_bas_butterworth_filter.setGeometry(QtCore.QRect(330, 10, 75, 31))
        self.apply_passe_bas_butterworth_filter.setObjectName("apply_passe_bas_butterworth_filter")

        self.apply_passe_haut_butterworth_filter = QtWidgets.QPushButton(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.apply_passe_haut_butterworth_filter.setGeometry(QtCore.QRect(740, 10, 75, 31))
        self.apply_passe_haut_butterworth_filter.setObjectName("apply_passe_haut_butterworth_filter")

        self.seuil_passe_haut_butterworth_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.seuil_passe_haut_butterworth_filter.setGeometry(QtCore.QRect(685, 10, 42, 31))
        self.seuil_passe_haut_butterworth_filter.setMinimum(1)
        self.seuil_passe_haut_butterworth_filter.setMaximum(50)
        self.seuil_passe_haut_butterworth_filter.setObjectName("seuil_passe_haut_butterworth_filter")

        self.seuil_passe_bas_butterworth_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.seuil_passe_bas_butterworth_filter.setGeometry(QtCore.QRect(275, 10, 42, 31))
        self.seuil_passe_bas_butterworth_filter.setMinimum(1)
        self.seuil_passe_bas_butterworth_filter.setMaximum(50)
        self.seuil_passe_bas_butterworth_filter.setObjectName("seuil_passe_bas_butterworth_filter")

        self.order_passe_haut_butterworth_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.order_passe_haut_butterworth_filter.setGeometry(QtCore.QRect(595, 10, 42, 31))
        self.order_passe_haut_butterworth_filter.setMinimum(1)
        self.order_passe_haut_butterworth_filter.setMaximum(50)
        self.order_passe_haut_butterworth_filter.setObjectName("order_passe_haut_butterworth_filter")

        self.order_passe_bas_butterworth_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.order_passe_bas_butterworth_filter.setGeometry(QtCore.QRect(185, 10, 42, 31))
        self.order_passe_bas_butterworth_filter.setMinimum(1)
        self.order_passe_bas_butterworth_filter.setMaximum(50)
        self.order_passe_bas_butterworth_filter.setObjectName("order_passe_bas_butterworth_filter")

        self.label_seuil_passe_bas_2 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.label_seuil_passe_bas_2.setGeometry(QtCore.QRect(250, 20, 47, 13))
        self.label_seuil_passe_bas_2.setObjectName("label_seuil_passe_bas_2")

        self.label_seuil_passe_haut_2 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.label_seuil_passe_haut_2.setGeometry(QtCore.QRect(660, 20, 47, 13))
        self.label_seuil_passe_haut_2.setObjectName("label_seuil_passe_haut_2")

        self.label_order_passe_bas_2 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.label_order_passe_bas_2.setGeometry(QtCore.QRect(155, 20, 47, 13))
        self.label_order_passe_bas_2.setObjectName("label_order_passe_bas_2")

        self.label_order_passe_haut_2 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_butterworth)
        self.label_order_passe_haut_2.setGeometry(QtCore.QRect(565, 20, 47, 13))
        self.label_order_passe_haut_2.setObjectName("label_order_passe_haut_2")

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_frequency_filtring_butterworth)


        # ================================================= #
        #          Partie de bas de filtre gaussien         #
        # ================================================= #
        self.main_body_bottom_part_frequency_filtring_gaussien = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_frequency_filtring_gaussien.setStyleSheet("#main_body_bottom_part_frequency_filtring_gaussien {\n"
                                                                            "    background-color: #C5FF95;\n"
                                                                            "    max-height: 50px;\n"
                                                                            "}")
        self.main_body_bottom_part_frequency_filtring_gaussien.setObjectName("main_body_bottom_part_frequency_filtring_gaussien")
        
        # Contenu de cette partie
        self.line_3 = QtWidgets.QFrame(self.main_body_bottom_part_frequency_filtring_gaussien)
        self.line_3.setGeometry(QtCore.QRect(430, 0, 3, 61))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.label_passe_bas_1 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_gaussien)
        self.label_passe_bas_1.setGeometry(QtCore.QRect(40, 16, 61, 20))
        self.label_passe_bas_1.setObjectName("label_passe_bas_1")

        self.label_passe_haut_1 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_gaussien)
        self.label_passe_haut_1.setGeometry(QtCore.QRect(460, 15, 61, 21))
        self.label_passe_haut_1.setObjectName("label_passe_haut_1")

        self.apply_passe_bas_gaussien_filter = QtWidgets.QPushButton(self.main_body_bottom_part_frequency_filtring_gaussien)
        self.apply_passe_bas_gaussien_filter.setGeometry(QtCore.QRect(330, 10, 75, 31))
        self.apply_passe_bas_gaussien_filter.setObjectName("apply_passe_bas_gaussien_filter")

        self.apply_passe_haut_gaussien_filter = QtWidgets.QPushButton(self.main_body_bottom_part_frequency_filtring_gaussien)
        self.apply_passe_haut_gaussien_filter.setGeometry(QtCore.QRect(740, 10, 75, 31))
        self.apply_passe_haut_gaussien_filter.setObjectName("apply_passe_haut_gaussien_filter")

        self.seuil_passe_haut_gaussien_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_frequency_filtring_gaussien)
        self.seuil_passe_haut_gaussien_filter.setGeometry(QtCore.QRect(680, 10, 42, 31))
        self.seuil_passe_haut_gaussien_filter.setMinimum(1)
        self.seuil_passe_haut_gaussien_filter.setMaximum(50)
        self.seuil_passe_haut_gaussien_filter.setObjectName("seuil_passe_haut_gaussien_filter")

        self.seuil_passe_bas_gaussien_filter = QtWidgets.QSpinBox(self.main_body_bottom_part_frequency_filtring_gaussien)
        self.seuil_passe_bas_gaussien_filter.setGeometry(QtCore.QRect(270, 10, 42, 31))
        self.seuil_passe_bas_gaussien_filter.setMinimum(1)
        self.seuil_passe_bas_gaussien_filter.setMaximum(50)
        self.seuil_passe_bas_gaussien_filter.setObjectName("seuil_passe_bas_gaussien_filter")

        self.label_seuil_passe_bas_1 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_gaussien)
        self.label_seuil_passe_bas_1.setGeometry(QtCore.QRect(230, 20, 47, 13))
        self.label_seuil_passe_bas_1.setObjectName("label_seuil_passe_bas_1")

        self.label_seuil_passe_haut_1 = QtWidgets.QLabel(self.main_body_bottom_part_frequency_filtring_gaussien)
        self.label_seuil_passe_haut_1.setGeometry(QtCore.QRect(640, 20, 47, 13))
        self.label_seuil_passe_haut_1.setObjectName("label_seuil_passe_haut_1")

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_frequency_filtring_gaussien)

        # ================================================= #
        #          Partie de bas de l'erosion               #
        # ================================================= #

        self.main_body_bottom_part_erosion = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_erosion.setStyleSheet("""
                                                            #main_body_bottom_part_erosion {
                                                                background-color: #C5FF95;
                                                                max-height: 50px;
                                                            }
                                                        """)
        self.main_body_bottom_part_erosion.setObjectName("main_body_bottom_part_erosion")

        # contenu de cette partie
        self.label_taille_element_structurant = QtWidgets.QLabel(self.main_body_bottom_part_erosion)
        self.label_taille_element_structurant.setGeometry(QtCore.QRect(270, 20, 71, 16))
        self.label_taille_element_structurant.setStyleSheet("#label_taille_element_structurant {\n"
                                                                        "height: 30px;\n"
                                                                        "}")
        self.label_taille_element_structurant.setObjectName("label_taille_element_structurant")
        
        self.apply_porphology_erosion = QtWidgets.QPushButton(self.main_body_bottom_part_erosion)
        self.apply_porphology_erosion.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.apply_porphology_erosion.setObjectName("apply_porphology_erosion")
        
        self.element_structurant_taille_erosion = QtWidgets.QSpinBox(self.main_body_bottom_part_erosion)
        self.element_structurant_taille_erosion.setGeometry(QtCore.QRect(350, 10, 42, 31))
        self.element_structurant_taille_erosion.setObjectName("element_structurant_taille_erosion")
        self.element_structurant_taille_erosion.setMinimum(1)
        self.element_structurant_taille_erosion.setMaximum(50)

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_erosion)

        # ================================================= #
        #          Partie de bas de dilatation              #
        # ================================================= #

        self.main_body_bottom_part_dilatation = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_dilatation.setStyleSheet("""
                                                            #main_body_bottom_part_dilatation {
                                                                background-color: #C5FF95;
                                                                max-height: 50px;
                                                            }
                                                        """)
        self.main_body_bottom_part_dilatation.setObjectName("main_body_bottom_part_dilatation")

        # contenu de cette partie
        self.label_taille_element_structurant_1 = QtWidgets.QLabel(self.main_body_bottom_part_dilatation)
        self.label_taille_element_structurant_1.setGeometry(QtCore.QRect(270, 20, 71, 16))
        self.label_taille_element_structurant_1.setStyleSheet("#label_taille_element_structurant_1 {\n"
                                                                        "height: 30px;\n"
                                                                        "}")
        self.label_taille_element_structurant_1.setObjectName("label_taille_element_structurant_1")
        
        self.apply_porphology_dilatation = QtWidgets.QPushButton(self.main_body_bottom_part_dilatation)
        self.apply_porphology_dilatation.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.apply_porphology_dilatation.setObjectName("apply_porphology_dilatation")
        
        self.element_structurant_taille_dilatation = QtWidgets.QSpinBox(self.main_body_bottom_part_dilatation)
        self.element_structurant_taille_dilatation.setGeometry(QtCore.QRect(350, 10, 42, 31))
        self.element_structurant_taille_dilatation.setObjectName("element_structurant_taille_dilatation")
        self.element_structurant_taille_dilatation.setMinimum(1)
        self.element_structurant_taille_dilatation.setMaximum(50)

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_dilatation)

        # ================================================= #
        #          Partie de bas de ouverture               #
        # ================================================= #

        self.main_body_bottom_part_ouverture = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_ouverture.setStyleSheet("""
                                                            #main_body_bottom_part_ouverture {
                                                                background-color: #C5FF95;
                                                                max-height: 50px;
                                                            }
                                                        """)
        self.main_body_bottom_part_ouverture.setObjectName("main_body_bottom_part_ouverture")

        # contenu de cette partie
        self.label_taille_element_structurant_2 = QtWidgets.QLabel(self.main_body_bottom_part_ouverture)
        self.label_taille_element_structurant_2.setGeometry(QtCore.QRect(270, 20, 71, 16))
        self.label_taille_element_structurant_2.setStyleSheet("#label_taille_element_structurant_2 {\n"
                                                                        "height: 30px;\n"
                                                                        "}")
        self.label_taille_element_structurant_2.setObjectName("label_taille_element_structurant_2")
        
        self.apply_porphology_ouverture = QtWidgets.QPushButton(self.main_body_bottom_part_ouverture)
        self.apply_porphology_ouverture.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.apply_porphology_ouverture.setObjectName("apply_porphology_ouverture")
        
        self.element_structurant_taille_ouverture = QtWidgets.QSpinBox(self.main_body_bottom_part_ouverture)
        self.element_structurant_taille_ouverture.setGeometry(QtCore.QRect(350, 10, 42, 31))
        self.element_structurant_taille_ouverture.setObjectName("element_structurant_taille_ouverture")
        self.element_structurant_taille_ouverture.setMinimum(1)
        self.element_structurant_taille_ouverture.setMaximum(50)

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_ouverture)

        # ================================================= #
        #          Partie de bas de fermeture               #
        # ================================================= #

        self.main_body_bottom_part_fermeture = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_fermeture.setStyleSheet("""
                                                            #main_body_bottom_part_fermeture {
                                                                background-color: #C5FF95;
                                                                max-height: 50px;
                                                            }
                                                        """)
        self.main_body_bottom_part_fermeture.setObjectName("main_body_bottom_part_fermeture")

        # contenu de cette partie
        self.label_taille_element_structurant_3 = QtWidgets.QLabel(self.main_body_bottom_part_fermeture)
        self.label_taille_element_structurant_3.setGeometry(QtCore.QRect(270, 20, 71, 16))
        self.label_taille_element_structurant_3.setStyleSheet("#label_taille_element_structurant_3 {\n"
                                                                        "height: 30px;\n"
                                                                        "}")
        self.label_taille_element_structurant_3.setObjectName("label_taille_element_structurant_3")
        
        self.apply_porphology_fermeture = QtWidgets.QPushButton(self.main_body_bottom_part_fermeture)
        self.apply_porphology_fermeture.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.apply_porphology_fermeture.setObjectName("apply_porphology_fermeture")
        
        self.element_structurant_taille_fermeture = QtWidgets.QSpinBox(self.main_body_bottom_part_fermeture)
        self.element_structurant_taille_fermeture.setGeometry(QtCore.QRect(350, 10, 42, 31))
        self.element_structurant_taille_fermeture.setObjectName("element_structurant_taille_fermeture")
        self.element_structurant_taille_fermeture.setMinimum(1)
        self.element_structurant_taille_fermeture.setMaximum(50)

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_fermeture)

        # ================================================= #
        #          Partie de bas de kmeans               #
        # ================================================= #

        self.main_body_bottom_part_kmeans = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_kmeans.setStyleSheet("""
                                                            #main_body_bottom_part_kmeans {
                                                                background-color: #C5FF95;
                                                                max-height: 50px;
                                                            }
                                                        """)
        self.main_body_bottom_part_kmeans.setObjectName("main_body_bottom_part_kmeans")

        # contenu de cette partie
        self.label_k = QtWidgets.QLabel(self.main_body_bottom_part_kmeans)
        self.label_k.setGeometry(QtCore.QRect(320, 20, 40, 10))
        self.label_k.setStyleSheet("#label_k {\n"
                                        "height: 30px;\n"
                                        "}")
        self.label_k.setObjectName("label_k")
        
        self.apply_kmeans = QtWidgets.QPushButton(self.main_body_bottom_part_kmeans)
        self.apply_kmeans.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.apply_kmeans.setObjectName("apply_kmeans")
        
        self.k = QtWidgets.QSpinBox(self.main_body_bottom_part_kmeans)
        self.k.setGeometry(QtCore.QRect(350, 10, 42, 31))
        self.k.setObjectName("k")
        self.k.setMinimum(1)
        self.k.setMaximum(50)

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_kmeans)

        # ================================================= #
        #              Partie de bas de hough               #
        # ================================================= #

        self.main_body_bottom_part_hough = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_hough.setStyleSheet("""
                                                            #main_body_bottom_part_hough {
                                                                background-color: #C5FF95;
                                                                max-height: 50px;
                                                            }
                                                        """)
        self.main_body_bottom_part_hough.setObjectName("main_body_bottom_part_hough")

        # contenu de cette partie
        self.label_threshold_hough = QtWidgets.QLabel(self.main_body_bottom_part_hough)
        self.label_threshold_hough.setGeometry(QtCore.QRect(320, 20, 40, 10))
        self.label_threshold_hough.setStyleSheet("#label_threshold_hough {\n"
                                        "height: 30px;\n"
                                        "}")
        self.label_threshold_hough.setObjectName("label_threshold_hough")
        
        self.apply_hough = QtWidgets.QPushButton(self.main_body_bottom_part_hough)
        self.apply_hough.setGeometry(QtCore.QRect(460, 10, 75, 31))
        self.apply_hough.setObjectName("apply_hough")
        
        self.threshold = QtWidgets.QSpinBox(self.main_body_bottom_part_hough)
        self.threshold.setGeometry(QtCore.QRect(350, 10, 42, 31))
        self.threshold.setObjectName("k")
        self.threshold.setMinimum(1)
        self.threshold.setMaximum(50)

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_hough)

        # ================================================= #
        #              Partie de bas de huffman             #
        # ================================================= #

        self.main_body_bottom_part_huffman = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_huffman.setStyleSheet("""
                                                            #main_body_bottom_part_huffman {
                                                                background-color: #C5FF95;
                                                                max-height: 50px;
                                                            }
                                                        """)
        self.main_body_bottom_part_huffman.setObjectName("main_body_bottom_part_huffman")

        # contenu de cette partie
        self.label_file_huffman = QtWidgets.QLabel(self.main_body_bottom_part_huffman)
        self.label_file_huffman.setGeometry(QtCore.QRect(260, 20, 100, 10))
        self.label_file_huffman.setStyleSheet("#label_file_hough {\n"
                                        "height: 30px;\n"
                                        "}")
        self.label_file_huffman.setObjectName("label_file_hough")
        
        self.apply_huffman = QtWidgets.QPushButton(self.main_body_bottom_part_huffman)
        self.apply_huffman.setGeometry(QtCore.QRect(500, 10, 75, 31))
        self.apply_huffman.setObjectName("apply_huffman")
        
        self.huffman_file_name = QLineEdit(self.main_body_bottom_part_huffman)
        self.huffman_file_name.setGeometry(QtCore.QRect(380, 10, 110, 31))
        self.huffman_file_name.setObjectName("huffman_file_name")

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_huffman)

        # ================================================= #
        #     Partie de bas de croissance de region         #
        # ================================================= #

        self.main_body_bottom_part_region_croissance = QtWidgets.QWidget(self.main_body)
        self.main_body_bottom_part_region_croissance.setStyleSheet("""
                                                            #main_body_bottom_part_region_croissance {
                                                                background-color: #C5FF95;
                                                                max-height: 50px;
                                                            }
                                                        """)
        self.main_body_bottom_part_region_croissance.setObjectName("main_body_bottom_part_region_croissance")

        # contenu de cette partie
        self.label_threshold_region_croissance = QtWidgets.QLabel(self.main_body_bottom_part_region_croissance)
        self.label_threshold_region_croissance.setGeometry(QtCore.QRect(200, 20, 40, 10))
        self.label_threshold_region_croissance.setStyleSheet("#label_threshold_region_croissance {\n"
                                        "height: 30px;\n"
                                        "}")
        self.label_threshold_region_croissance.setObjectName("label_threshold_region_croissance")

        self.threshold_region_croissance = QtWidgets.QSpinBox(self.main_body_bottom_part_region_croissance)
        self.threshold_region_croissance.setGeometry(QtCore.QRect(227, 10, 42, 31))
        self.threshold_region_croissance.setObjectName("k")
        self.threshold_region_croissance.setMinimum(1)

        self.label_y_region_croissance = QtWidgets.QLabel(self.main_body_bottom_part_region_croissance)
        self.label_y_region_croissance.setGeometry(QtCore.QRect(360, 20, 40, 10))
        self.label_y_region_croissance.setStyleSheet("#label_y_region_croissance {\n"
                                        "height: 30px;\n"
                                        "}")
        self.label_y_region_croissance.setObjectName("label_y_region_croissance")

        self.y_region_croissance = QtWidgets.QSpinBox(self.main_body_bottom_part_region_croissance)
        self.y_region_croissance.setGeometry(QtCore.QRect(375, 10, 42, 31))
        self.y_region_croissance.setObjectName("y")
        self.y_region_croissance.setMinimum(0)
        self.y_region_croissance.setMaximum(2000)
        self.y_region_croissance.setValue(100)
        
        self.label_x_region_croissance = QtWidgets.QLabel(self.main_body_bottom_part_region_croissance)
        self.label_x_region_croissance.setGeometry(QtCore.QRect(430, 20, 40, 10))
        self.label_x_region_croissance.setStyleSheet("#label_x_region_croissance {\n"
                                        "height: 30px;\n"
                                        "}")
        self.label_x_region_croissance.setObjectName("label_x_region_croissance")

        self.x_region_croissance = QtWidgets.QSpinBox(self.main_body_bottom_part_region_croissance)
        self.x_region_croissance.setGeometry(QtCore.QRect(445, 10, 42, 31))
        self.x_region_croissance.setObjectName("x")
        self.x_region_croissance.setMinimum(0)
        self.x_region_croissance.setMaximum(2000)
        self.x_region_croissance.setValue(100)

        self.add_region_croissance = QtWidgets.QPushButton(self.main_body_bottom_part_region_croissance)
        self.add_region_croissance.setGeometry(QtCore.QRect(500, 10, 75, 31))
        self.add_region_croissance.setObjectName("add_region_croissance")

        self.apply_region_croissance = QtWidgets.QPushButton(self.main_body_bottom_part_region_croissance)
        self.apply_region_croissance.setGeometry(QtCore.QRect(600, 10, 75, 31))
        self.apply_region_croissance.setObjectName("apply_region_croissance")
        

        # Ajouter cette partie au partie de centre de fenetre principale pour qu'elle soit en bas
        self.verticalLayout_4.addWidget(self.main_body_bottom_part_region_croissance)

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing"))
        
        self.left_menu_base_actions.setText(_translate("MainWindow", "Base actions"))
        self.left_menu_binarization.setText(_translate("MainWindow", "Binarization"))
        self.left_menu_filters.setText(_translate("MainWindow", "Filters"))
        self.left_menu_frequency_feltring.setText(_translate("MainWindow", "Frequency Filters"))
        self.left_menu_contours.setText(_translate("MainWindow", "Contours"))
        self.left_menu_morphology.setText(_translate("MainWindow", "Morphology"))
        self.left_menu_segmentation.setText(_translate("MainWindow", "Segmentation"))
        self.left_menu_points_of_interest.setText(_translate("MainWindow", "Points Of Interest"))
        self.left_menu_compression.setText(_translate("MainWindow", "Compression"))
        self.left_menu_save_image.setText(_translate("MainWindow", "Save image"))
        
        self.manual_thresholding.setText(_translate("MainWindow", "Manual Thresholding"))
        self.otsu_thresholding.setText(_translate("MainWindow", "Otsu Thresholding"))
        
        self.inverse_image.setText(_translate("MainWindow", "Inverse Image"))
        self.rotate_image.setText(_translate("MainWindow", "Rotate Image"))
        self.resize_image.setText(_translate("MainWindow", "Resize Image"))
        self.histogramme.setText(_translate("MainWindow", "Histogramme"))
        self.equalize.setText(_translate("MainWindow", "Equalize"))
        self.stretch.setText(_translate("MainWindow", "Stretch"))
        
        self.gaussien.setText(_translate("MainWindow", "Gaussien"))
        self.mean.setText(_translate("MainWindow", "Mean"))
        self.median.setText(_translate("MainWindow", "Median"))
        
        self.load_image.setText(_translate("MainWindow", "Load Image"))
        
        self.label_rotation_angle.setText(_translate("MainWindow", "Rotation Angle"))
        self.button_rotate.setText(_translate("MainWindow", "Rotate"))
        
        self.label_pecentage.setText(_translate("MainWindow", "Percentage"))
        self.button_percentage.setText(_translate("MainWindow", "Resize"))
        
        self.label_width.setText(_translate("MainWindow", "Width"))
        self.label_height.setText(_translate("MainWindow", "Height"))
        self.button_width_height.setText(_translate("MainWindow", "Resize"))
        
        self.otsu_threshold.setText(_translate("MainWindow", "Otsu Threshold :"))
        self.otsu_threshold_value.setText(_translate("MainWindow", "00"))
        
        self.label_otsu_manual_threshold.setText(_translate("MainWindow", "Otsu Threshold"))
        self.button_threshold.setText(_translate("MainWindow", "Threshold"))
        self.label_taille_filter_mean.setText(_translate("MainWindow", "Filter Size"))
        self.label_taille_filter_median.setText(_translate("MainWindow", "Filter Size"))
        self.label_taille_filter_gaussien.setText(_translate("MainWindow", "Filter Size"))
        self.button_apply_mean_filter.setText(_translate("MainWindow", "Apply Filter"))
        self.button_apply_median_filter.setText(_translate("MainWindow", "Apply Filter"))
        self.label_ecartType_gaussien_filter.setText(_translate("MainWindow", "Ecart Type"))
        self.button_apply_gaussien_filter.setText(_translate("MainWindow", "Apply Filter"))
        
        self.ideal.setText(_translate("MainWindow", "Ideal"))
        self.butterworth.setText(_translate("MainWindow", "Butter Worth"))
        self.gauss.setText(_translate("MainWindow", "Gaussien"))
        
        self.image_original.setText(_translate("MainWindow", "Original Im"))
        self.image_current.setText(_translate("MainWindow", "Modified Im"))
        self.image_orig.setText(_translate("MainWindow", "Remove All"))
        
        self.label_passe_bas.setText(_translate("MainWindow", "Passe Bas"))
        self.label_passe_haut.setText(_translate("MainWindow", "Passe Haut"))
        self.apply_passe_bas_ideal_filter.setText(_translate("MainWindow", "Apply"))
        self.apply_passe_haut_ideal_filter.setText(_translate("MainWindow", "Apply"))
        self.label_seuil_passe_bas.setText(_translate("MainWindow", "Seuil"))
        self.label_seuil_passe_haut.setText(_translate("MainWindow", "Seuil"))
        self.label_passe_bas_1.setText(_translate("MainWindow", "Passe Bas"))
        self.label_passe_haut_1.setText(_translate("MainWindow", "Passe Haut"))
        self.apply_passe_bas_gaussien_filter.setText(_translate("MainWindow", "Apply"))
        self.apply_passe_haut_gaussien_filter.setText(_translate("MainWindow", "Apply"))
        self.label_seuil_passe_bas_1.setText(_translate("MainWindow", "Seuil"))
        self.label_seuil_passe_haut_1.setText(_translate("MainWindow", "Seuil"))
        self.label_passe_bas_2.setText(_translate("MainWindow", "Passe Bas"))
        self.label_passe_haut_2.setText(_translate("MainWindow", "Passe Haut"))
        self.apply_passe_bas_butterworth_filter.setText(_translate("MainWindow", "Apply"))
        self.apply_passe_haut_butterworth_filter.setText(_translate("MainWindow", "Apply"))
        self.label_seuil_passe_bas_2.setText(_translate("MainWindow", "Seuil"))
        self.label_seuil_passe_haut_2.setText(_translate("MainWindow", "Seuil"))
        self.label_order_passe_bas_2.setText(_translate("MainWindow", "Order"))
        self.label_order_passe_haut_2.setText(_translate("MainWindow", "Order"))
        self.sobel.setText(_translate("MainWindow", "Sobel"))
        self.robert.setText(_translate("MainWindow", "Robert"))
        self.laplacien.setText(_translate("MainWindow", "Laplacien"))
        self.gradiant.setText(_translate("MainWindow", "Gradient"))
        self.erosion.setText(_translate("MainWindow", "Erosion"))
        self.dilatation.setText(_translate("MainWindow", "Dilatation"))
        self.ouverture.setText(_translate("MainWindow", "Ouverture"))
        self.fermeture.setText(_translate("MainWindow", "Fermeture"))

        self.apply_porphology_erosion.setText(_translate("MainWindow", "Apply"))
        self.label_taille_element_structurant.setText(_translate("MainWindow", "Taille ES"))

        self.apply_porphology_dilatation.setText(_translate("MainWindow", "Apply"))
        self.label_taille_element_structurant_1.setText(_translate("MainWindow", "Taille ES"))

        self.apply_porphology_ouverture.setText(_translate("MainWindow", "Apply"))
        self.label_taille_element_structurant_2.setText(_translate("MainWindow", "Taille ES"))

        self.apply_porphology_fermeture.setText(_translate("MainWindow", "Apply"))
        self.label_taille_element_structurant_3.setText(_translate("MainWindow", "Taille ES"))

        self.kmeans.setText(_translate("MainWindow", "K - Means"))
        self.region_croissance.setText(_translate("MainWindow", "Region Croissance"))
        self.regions_partition.setText(_translate("MainWindow", "Regions Partition"))

        self.hough.setText(_translate("MainWindow", "Hough"))

        self.huffman.setText(_translate("MainWindow", "HuffMan"))
        self.lzw.setText(_translate("MainWindow", "LZW"))

        self.label_k.setText(_translate("MainWindow", "K"))
        self.apply_kmeans.setText(_translate("MainWindow", "Apply"))

        self.label_threshold_hough.setText(_translate("MainWindow", "Seuil"))
        self.apply_hough.setText(_translate("MainWindow", "Apply"))

        self.label_file_huffman.setText(_translate("MainWindow", "Output File Name"))
        self.apply_huffman.setText(_translate("MainWindow", "Apply"))

        self.label_threshold_region_croissance.setText(_translate("MainWindow", "Seuil"))
        self.label_y_region_croissance.setText(_translate("MainWindow", "Y"))
        self.label_x_region_croissance.setText(_translate("MainWindow", "X"))
        self.add_region_croissance.setText(_translate("MainWindow", "Add"))
        self.apply_region_croissance.setText(_translate("MainWindow", "Apply"))