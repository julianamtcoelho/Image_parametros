import cv2 as cv
from matplotlib import pyplot as plt

def LaminaTransCorImage (image, color_space, flagprint):
    
    if color_space == 'gray':
        image = cv.Color(image, cv.COLOR_RGB2GRAY)
        
    elif color_space == 'ycrb' or color_space == 'ycc':
        image = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
        
    elif color_space == 'lab':
        image = cv.cvtColor(image, cv.COLOR_BGR2LAB) 
    
    elif color_space == 'xyz':
        image = cv.cvtColor(image, cv.COLOR_BGR2XYZ) 
    
    elif color_space == 'hls':
        image = cv.cvtColor(image, cv.COLOR_BGR2HLS) 
        
        
    else:
        image = cv.cvtColor(image, cv.COLOR_RGB2RGBA)
        
    if (flagprint == 1):
        plt.figure(figsize = (20,10))
        plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        
        
        
    channel = '012'
    if channel != 'all':
        channels = cv.split(image)
        channel_indices =[]
        for char in channel:
            channel_indices.append(int(char))
        image = image[:, :, channel_indices]
        if len(image.shape) == 2:
            image.reshape(img.shape[0], img.shape[1], 1)
      
        
    return image



