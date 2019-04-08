# pancreas-imaging
Pancreas image sorting script for John Brennan, 2019-04-05

Simple Python script to read image metadata (specifically transplantability consensus field) from collated_scores.xlsx and sort a directory of images into good and bad accordingly.  Output is a pair of square cropped images in directory 'good_images' or 'bad_images':

```
./<image_number>_left.png 
./<image_number>_right.png  
```

Note that the source images are assumed to be in landscape format; the output images will generally contain some overlapping area.  The source images are in Sharepoint at:

```
https://newcastle.sharepoint.com/:f:/r/sites/DigitalInstitute581/Shared%20Documents/Research/RSE%20Team/Projects/Pancreas%20Transplant%20Viability/Training%20Images?csf=1&e=00H1NQ
```

Script requires pandas and pillow Python libraries (former installed by default in Anaconda, the other requires:

```
conda install -c anaconda pillow
```


