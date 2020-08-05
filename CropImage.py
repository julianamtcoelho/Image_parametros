import cv2 as cv
from matplotlib import pyplot as plt


def LaminaCropImage(image, width,flagprint):   
    height = int((width/ image.shape[1]) * image.shape[0])
    image = cv.resize(image,(width, height), interpolation=cv.INTER_AREA)
    
    
    if (flagprint == 1):
        plt.figure(figsize = (20,10))
        plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))    
    
    return image