import matplotlib.pyplot as plt  # type: ignore
from VPO.BaseFunctions import *
from VPO.Binarisations import *
from VPO.Egalisation_Etirement import *
from VPO.Spatial_Filters import *
from VPO.Frequentiel_Filters import *
from VPO.Morphologie_Mathématique import *
from VPO.Contours_Extraction import *
from VPO.Image_Segmentation import *
from VPO.Hough import hough_transform

# image = read_image("im1.png") 
# plt.imshow(image)
# plt.show()

# image = read_image("im1.png")
# save_image(image, "hamada.tif")

# image = read_image("cat.jpeg")
# image = negative_image(image)
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# image = rotate_image(image, 45)
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# image = resize_image(image, (6000, 6000))
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# image = binarisation_globale_manual(image, 127)
# plt.imshow(image, cmap="gray")
# plt.show()

# image = read_image("car.jpg")
# image = binarisation_globale_otsu(image)
# plt.imshow(image, cmap="gray")
# plt.show()

# image = read_image("car.jpg")
# show_hist(image)

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# show_hist(image)
# image = egaliser_image(image)
# plt.imshow(image)
# plt.show()
# show_hist(image)

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# show_hist(image)
# image = etirer_image(image)
# plt.imshow(image)
# plt.show()
# show_hist(image)

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# image = filtre_gaussien(image, 1, 3)
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# image = filtre_moyenneur(image, 3)
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# image = filtre_median(image, 3)
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# image = getBasIdealFilter(image, 3)
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# image = getBasButterWorthFilter(image, 3, 2)
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# image = getBasGaussienFilter(image, 3)
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# image = getHautIdealFilter(image, 3)
# plt.imshow(image)
# plt.show()

# image = read_image("car.jpg")
# plt.imshow(image)
# plt.show()
# image = getHautButterWorthFilter(image, 3, 2)
# plt.imshow(image)
# plt.show()

# image = read_image("im2.png")
# plt.imshow(image)
# plt.show()

# es = np.array([[0, 1, 0],
#                 [1, 1, 1],
#                 [0, 1, 0]], dtype=np.uint8)
# image = erosion(image, es)
# plt.imshow(image, cmap="gray")
# plt.show()

# image = read_image("car.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(image)
# plt.show()
# image = sobel_operator(image)
# plt.imshow(image, cmap="gray")
# plt.show()
# print(image)

# image = read_image("car.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(image)
# plt.show()
# image = laplacian_operator(image)
# plt.imshow(image, cmap="gray")
# plt.show()
# print(image)

# image = read_image("car.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(image)
# plt.show()
# image = robert_operator(image)
# plt.imshow(image, cmap="gray")
# plt.show()
# print(image)

# image = read_image("car.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(image, cmap="gray")
# plt.show()
# image = region_Croissance(image, [(100,100)], 60)
# plt.imshow(image, cmap="gray")
# plt.show()
# print(image)

# image = read_image("car.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(image, cmap="gray")
# plt.show()
# image = k_means_Segmentation(image, 2)
# plt.imshow(image, cmap="gray")
# plt.show()
# print(image)

image = read_image("car.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image, cmap="gray")
plt.show()

# Appliquer la transformation de Hough pour détecter les points d'intérêt
hough_lines = hough_transform(image, 10)

# Tracer les lignes détectées sur l'image originale
for rho, theta in hough_lines:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image, (x1, y1), (x2, y2), (54, 54, 255), 2)

# Afficher l'image avec les lignes détectées
cv2.imshow('Lines Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()