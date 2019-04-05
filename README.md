# pancreas-imaging
Pancreas image sorting script for John Brennan, 2019-04-05

Requires pandas and pillow Python libraries (former installed by default in Anaconda, the other requires:

```
conda install -c anaconda pillow
```

Simple Python script to read image metadata (specifically transplantability consensus field) from collated_scores.xlsx and sort a directory of images into good and bad accordingly.  Output is a pair of square images:

```
&lt;image_number&gt;_left.png 
&lt;image_number&gt;_right.png  
```
