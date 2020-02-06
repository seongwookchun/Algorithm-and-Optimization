# importing os module 
import os 
from glob import glob
import re
# Function to rename multiple files 

d_reordering = dict()
for idx, filename in enumerate(glob("./*.png")):
	num = re.findall('\d+', filename)[0]
	d_reordering[int(num)] = filename
    # dst ="formingHeapStructure_" + '{:03d}'.format(idx) + ".png"
    # src =filename
    # # dst ='xyz'+ dst
          
    # # rename() function will 
    # # rename all the files 
    # # os.rename(src, dst) 
    # print('{:03d}'.format(idx), filename)

sorted(d_reordering)#, key=lambda x: x[0])

print(d_reordering)