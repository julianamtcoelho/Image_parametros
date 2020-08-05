import cv2 as cv
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


def LaminaSeg (image, original, n_clusters,flagprint):
    reshaped = image.reshape(image.shape[0] * image.shape[1], image.shape[2])
    if n_clusters < 2:
        num_clusters = 2
    num_Clusters = max(2, n_clusters)
    kmeans = KMeans(n_clusters=num_Clusters, n_init=40, max_iter=500).fit(reshaped)

    clustering = np.reshape(np.array(kmeans.labels_, dtype=np.uint8), (image.shape[0], image.shape[1]))

    sorted_labels = sorted([n for n in range(num_Clusters)],
    key=lambda x: -np.sum(clustering == x))

    kmeans_image = np.zeros(image.shape[:2], dtype=np.uint8)
    for i, label in enumerate(sorted_labels):
        kmeans_image[clustering == label] = int((255) / (num_Clusters - 1)) * i
        
    concatenated_image = np.concatenate((original, 193 * np.ones((original.shape[0], int(0.0625 * original.shape[1]), 3),
    dtype=np.uint8),cv.cvtColor(kmeans_image, cv.COLOR_GRAY2BGR)), axis=1)
    
    if (flagprint == 1):
        fig, axes = plt.subplots(ncols=2, figsize=(15,8), sharex=True, sharey=True)   
        ax = axes.ravel()
        ax[0].imshow(kmeans_image)
        ax[0].set_title('Kmeans Image')
        ax[1].imshow(kmeans_image,'gray')
        ax[1].set_title('Binary Image')
                   
        
        '''plt.figure(figsize = (15,8))
        plt.imshow(kmeans_image)
    
        plt.figure(figsize = (15,8))
        plt.imshow(kmeans_image,'gray')'''
    
    return concatenated_image, kmeans_image
