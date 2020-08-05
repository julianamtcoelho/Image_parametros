from skimage.measure import regionprops
import pandas as pd


def LaminaParametros(labels): 
    props = regionprops(labels)
    # exclude the bar on the bottom left:
    props = [p for p in props if p['centroid'][0]<950 and p['centroid'][1]>400]
    
    # get the sizes for each of the remaining objects and store in dataframe
    entries = []
    for p in props:
        entry = [p['label'], p['area'], p['perimeter'],p['eccentricity'] ,p['solidity'],p['orientation'],p['bbox_area'],p['extent'],*p['centroid']]
        entries.append(entry)
        
        
    df = pd.DataFrame(entries, columns= ['label', 'area','perimeter','eccentricity','solidity', 'orientation','bbox_area','extent', 'centroid_y', 'centroid_x'])
    df['roundness']=df['perimeter'] *df['perimeter'] /df['area']
    
    return df