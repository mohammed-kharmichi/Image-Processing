import cv2 # type: ignore
import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
import math
import os
from bitstring import BitArray # type: ignore



# Analyser l'image pour déterminer la fréquence de chaque pixel.
# Construire un arbre de Huffman basé sur ces fréquences.
# Générer des codes de Huffman à partir de l'arbre.
# Encoder l'image en utilisant ces codes.
# Écrire le résultat encodé dans un fichier, ainsi que les informations nécessaires pour décoder (comme la table des codes).

def huffman_compression(image, output_filename):

    # Convertir l'image en une chaîne de caractères
    data = ''.join(map(chr, image.flatten()))

    # Compter les occurrences de chaque caractère
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1

    # Créer une file de priorité pour les caractères et leurs fréquences
    pq = [(freq[char], char) for char in freq]

    # Construction de l'arbre de Huffman
    while len(pq) > 1:
        left_freq, left_char = pq.pop(0)
        right_freq, right_char = pq.pop(0)
        pq.append((left_freq + right_freq, (left_char, right_char)))

    huffman_tree = pq[0][1]

    # Créer le dictionnaire des codes de Huffman
    codes = {}

    def build_codes(node, code=''):
        if isinstance(node, tuple):
            build_codes(node[0], code + '0')
            build_codes(node[1], code + '1')
        else:
            codes[node] = code

    build_codes(huffman_tree)

    # Encoder les données avec Huffman
    encoded_data = BitArray()
    for char in data:
        encoded_data.append(BitArray(bin=codes[char]))

    # Enregistrer les données compressées dans un fichier binaire
    with open(output_filename, 'wb') as file:
        file.write(encoded_data.tobytes())
































def LZW(image):
    # Convertir l'image en une chaîne de caractères
    data = ''.join(map(chr, image.flatten()))

    # Initialiser le dictionnaire LZW avec les valeurs ASCII
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256  # Prochain code disponible dans le dictionnaire

    compressed_data = []  # Liste pour stocker les codes compressés
    current_code = ''  # Chaîne de caractères vide pour stocker le code actuel

    for symbol in data:
        if current_code + symbol in dictionary:  # Vérifier si le code actuel + le symbole est dans le dictionnaire
            current_code += symbol
        else:
            compressed_data.append(dictionary[current_code])  # Ajouter le code actuel à la liste compressée
            dictionary[current_code + symbol] = next_code  # Ajouter le nouveau code au dictionnaire
            next_code += 1  # Mettre à jour le prochain code disponible
            current_code = symbol  # Réinitialiser le code actuel au symbole seul

    compressed_data.append(dictionary[current_code])  # Ajouter le dernier code actuel à la liste compressée

    # Calculer la taille de l'image compressée
    compressed_size = len(compressed_data) * 2  # Chaque code est stocké sur 2 octets

    # Vérifier si la taille de l'image compressée est inférieure à celle de l'image originale
    original_size = image.size * image.itemsize  # Taille de l'image originale en octets

    # Afficher les résultats
    print("Taille de l'image compressée:", compressed_size)
    print("Taille de l'image originale:", original_size)

    if compressed_size < original_size:
        print(" => La taille de l'image compressée est inférieure à celle de l'image originale.")
    else:
        print(" => La taille de l'image compressée est égale ou supérieure à celle de l'image originale.")

    # Enregistrer l'image compressée
    output_filename = "CompresseLzw"  # Nom du fichier compressé
    with open(output_filename, 'wb') as file:
        for code in compressed_data:
            file.write(code.to_bytes(2, byteorder='big'))  # Écrire chaque code compressé sur 2 octets en big endian


