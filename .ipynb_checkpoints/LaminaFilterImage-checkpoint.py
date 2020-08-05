import cv2 as cv
from matplotlib import pyplot as plt

def LaminaFilterImage (image, typefilter, kSize, flagprint):
    if (typefilter=='median'):
        median_filtered_image = cv.medianBlur(src=image, ksize=kSize)
        if (flagprint == 1):
            plt.figure(figsize = (20,10))
            plt.imshow(cv.cvtColor(median_filtered_image, cv.COLOR_BGR2RGB))
            #set_title('Median Filter Image')
                    
    elif (typefilter == 'gaussian'):
        median_filtered_image = cv.GaussianBlur(image, (kSize,kSize),0)
        if (flagprint == 1):
            plt.figure(figsize = (20,10))
            plt.imshow(cv.cvtColor(median_filtered_image, cv.COLOR_BGR2RGB))
            #set_title('Gaussian Filter Image')
    elif (typefilter == 'nonlocalmeans'):
        median_filtered_image = cv.fastNlMeansDenoisingColored(image,None,10,10,7,21)
        if (flagprint == 1):
            plt.figure(figsize = (20,10))
            plt.imshow(cv.cvtColor(median_filtered_image, cv.COLOR_BGR2RGB))
            #set_title('NonLOcalMeans Filter Image')
            
    else:
        median_filtered_image1= cv.medianBlur(src=image, ksize=kSize)
        median_filtered_image2 = cv.GaussianBlur(image, (kSize,kSize),0)
        median_filtered_image = cv.fastNlMeansDenoisingColored(image,None,10,10,7,21)
        
        if (flagprint == 1):
            fig, axes = plt.subplots(ncols=4, figsize=(15,7), sharex=True, sharey=True)   
            ax = axes.ravel()
            ax[0].imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
            ax[0].set_title('Original Image')
            ax[1].imshow(cv.cvtColor(median_filtered_image1, cv.COLOR_BGR2RGB))
            ax[1].set_title('Median Filter Image')
            ax[2].imshow(cv.cvtColor(median_filtered_image2, cv.COLOR_BGR2RGB))
            ax[2].set_title('Gaussian Filter Image')
            ax[3].imshow(cv.cvtColor(median_filtered_image, cv.COLOR_BGR2RGB))
            ax[3].set_title('NonLocalMeans')
            
            
            for a in ax:
                a.set_axis_off()
    
            fig.tight_layout()
            plt.show()
        
           
            
    return median_filtered_image
