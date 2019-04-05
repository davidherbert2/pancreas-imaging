# -*- coding: utf-8 -*-
"""
Reads Excel spreadsheet containing pancreas image metadata assuming:
    
    (1) The spreadsheet and images reside in the same directory as this script
    (2) The metadata is stored in 'Sheet1'
    (3) Image number (integer) resides in column A
    (4) Decision column is consensus on transplantability in column AE
    (5) Images are all in landscape format, or at worst square already
    (6) Each image is required to be cropped into two (probably overlapping) square images
    
Created on Thu Apr  4 13:33:33 2019

@author: ndh114
"""

import os
import math
import pandas as pd
from PIL import Image

# Ensure trailing separator
scriptdir = os.path.normpath(os.path.dirname(__file__))

# Properties of the specific Excel workbook structure
workbook = os.path.join(scriptdir, 'collated_scores.xlsx')
sheet = 'Sheet1'
columns = 'A,AE',
skiprows = 4

# Where to output the cut and sorted images
good_images = os.path.join(scriptdir, 'good_images')
if not os.path.exists(good_images):
    os.makedirs(good_images)
bad_images = os.path.join(scriptdir, 'bad_images')
if not os.path.exists(bad_images):
    os.makedirs(bad_images)

# Read workbook sheet into a Pandas dataframe (using 'columns' in the usecols arg creates a spurious tuple)
df = pd.read_excel(workbook, sheetname = sheet, usecols = 'A,AE', skiprows = skiprows)
for index, row in df.iterrows():
    if not math.isnan(row[0]):
        # Looks like sensible data
        image_number = int(row[0])
        consensus = row[1]
        print('Image {} consensus {}'.format(image_number, consensus))
        # Read in the image and get its size (assume for the moment all are landscape format)
        img = Image.open(os.path.join(scriptdir, '{}.png'.format(image_number)))
        img_width, img_height = img.size
        print('Size is {} x {}'.format(img_width, img_height))
        if img_height < img_width:
            print('Landscape format - cropping out square regions')
            # Left crop
            left_area = (0, 0, img_height, img_height)
            img_cropped_left = img.crop(left_area)            
            # Right crop
            right_area = (img_width - img_height, 0, img_width, img_height)
            img_cropped_right = img.crop(right_area)
            # Save new square images
            img_cropped_left.save(os.path.join(scriptdir, '{}_images'.format(consensus.lower()), '{}_left.png'.format(image_number)), 'PNG')
            img_cropped_right.save(os.path.join(scriptdir, '{}_images'.format(consensus.lower()), '{}_right.png'.format(image_number)), 'PNG')            
        elif img_height == img_width:
            print('Image is square - nothing to do')
            img.save(os.path.join(scriptdir, '{}_images'.format(consensus.lower()), '{}.png'.format(image_number)), 'PNG')            
        else:
            print('Portrait format - not supported')