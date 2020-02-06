# importing os module 
import os 
from glob import glob
# Function to rename multiple files 
      
for idx, filename in enumerate(glob("./*.png")):
    dst ="formingHeapStructure_" + '{:03d}'.format(idx) + ".png"
    src =filename 
    # dst ='xyz'+ dst 
          
    # rename() function will 
    # rename all the files 
    # os.rename(src, dst) 
    print('{:03d}'.format(idx), filename)