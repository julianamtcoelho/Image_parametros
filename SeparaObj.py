from skimage.morphology import binary_erosion
from skimage.morphology import square
from scipy import ndimage as ndi
import cv2 as cv

from skimage.segmentation import watershed
from skimage.feature import peak_local_max
import imutils
import numpy as np
from matplotlib import pyplot as plt

#image = binary_erosion( k_means_image, square(2))


def LaminaSeparaObj (image, kernel, dist, flagprint,image_channel_settled):
    '''kernel = np.ones((20,20),np.uint8)
    opening = cv2.morphologyEx(k_means_image, cv2.MORPH_OPEN, kernel)
    plt.imshow(opening, cmap="gray")'''

    if (dist == 'edt'):
        distance = ndi.distance_transform_edt(image)
    else:
        distance = ndi.distance_transform_cdt(image)
    
    
    #image = k_means_image
    # Now we want to separate the two objects in image
    # Generate the markers as local maxima of the distance to the background
   
    local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((kernel,kernel)),
                            labels=image)
    markers = ndi.label(local_maxi)[0]
    labels = watershed(-distance, markers, mask=image)
    
    if (flagprint == 1):
        fig, axes = plt.subplots(ncols=3, figsize=(15, 8), sharex=True, sharey=True)
        ax = axes.ravel()
        
        ax[0].imshow(cv.cvtColor(image_channel_settled, cv.COLOR_BGR2RGB))
        ax[0].set_title('Original Image')
        ax[1].imshow(-distance, cmap=plt.cm.gray)
        ax[1].set_title('Distances')
        ax[2].imshow(labels, cmap=plt.cm.nipy_spectral)
        ax[2].set_title('Separated objects')

        for a in ax:
            a.set_axis_off()

        fig.tight_layout()
        plt.show()
        
    return image, labels, distance