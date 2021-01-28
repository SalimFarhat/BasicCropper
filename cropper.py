import os
import PIL
import glob
from PIL import Image
#put the directory below
dfiles = os.listdir('#')
all_files = [f for f in dfiles if 'Scan0' in f and f.endswith(('.jpg', '.png'))]
for ima in all_files:
    img = Image.open(ima)
    #Adjust following parameters to crop picture as required
    x = 5
    y = 5
    width = 1550
    height = 2150
    img = img.crop((x, y, width, height))
    #adjust following to save the file
    img.save('r_'+ima, optimize=True, quality=30)
