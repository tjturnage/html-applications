# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:32:33 2019

@author: tjtur

Requires Python 3 for pathlib
"""

import os
import re
import shutil
import pathlib

# pick directory with images to loop
image_dir = 'C:/data/20080608/KDTX/images/mosaic/005'
#image_dir = 'C:/data/20190601/satellite/stage'

im_dir = pathlib.PurePath(image_dir)
e_date = im_dir.parts[2]
if im_dir.parts[3] == 'satellite':
    page_title = e_date + ' satellite'
    loop_description = 'Satellite and Lightning<br>'
else:
    e_radar = im_dir.parts[3]
    e_slice = im_dir.parts[-1]
    e_slice = e_slice[0:2] + '.' + e_slice[2:4]
    if e_slice[0] == '0':
        e_slice = e_slice[1:]
    page_title = e_date + ' ' + e_radar + ' - ' + e_slice + ' deg'
    loop_description = 'Radar Velocity products derived with WDSS-II  (<a href="http://www.wdssii.org" target="_blank">http://www.wdssii.org/</a>)<br>'

# following file has to be copied into image directory
# available at https://github.com/tjturnage/resources for download
# if not manually putting into image directory, will need to note it's location and execute the following
# two commands
js_src = 'C:/data/scripts/resources/hanis_min.js'
shutil.copyfile(js_src,os.path.join(image_dir,'hanis_min.js'))

# there will be an index.html file created in the image directory to be subsequently opened in an internet browser
index_path = os.path.join(image_dir,'index.html')
these_files = os.listdir(image_dir)

# build list of image filenames
file_str = ''
for f in (these_files):
    if (re.search('png',f) is not None) or (re.search('png',f) is not None):
        file_str = file_str + f + ', ' 

#trim unwanted characters from string
file_str = file_str[0:-2]

# first part of html code
html_1 = '<!doctype html>\
<html>\
<head>\
<meta charset="utf-8">\
<title>' + page_title + '</title>\
<script type="text/javascript" src="hanis_min.js"></script>\
<style>\
body {\
	background-color: #434343;\
	color: white;\
	font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;\
	font-size: 12px;\
	text-align: center;\
}\
#container {\
	position: relative;\
	width: 1100px;\
	margin: 0 auto 0 auto;\
}\
#hanis {\
	background-color: #AEAEAE;\
}\
a, a:link, a:visited {\
	color: lightblue;\
}\
a:hover {\
	color: lightgreen;\
}\
</style>\
</head>\
\
<body onload="HAniS.setup(\'filenames = '

"""
Example of filenames list...
('filenames = 'HRRRMW_prec_radar_000.png, HRRRMW_prec_radar_001.png, HRRRMW_prec_radar_002.png, HRRRMW_prec_radar_003.png, HRRRMW_prec_radar_004.png, HRRRMW_prec_radar_005.png, HRRRMW_prec_radar_006.png, HRRRMW_prec_radar_007.png, HRRRMW_prec_radar_008.png, HRRRMW_prec_radar_009.png, HRRRMW_prec_radar_010.png, HRRRMW_prec_radar_011.png, HRRRMW_prec_radar_012.png, HRRRMW_prec_radar_013.png, HRRRMW_prec_radar_014.png, HRRRMW_prec_radar_015.png, HRRRMW_prec_radar_016.png, HRRRMW_prec_radar_017.png, HRRRMW_prec_radar_018.png\ncontrols = startstop, speed, step, looprock, zoom\ncontrols_style = display:flex;flex-flow:row;\nbuttons_style = flex:auto;margin:2px;cursor:pointer;\nbottom_controls = toggle\ntoggle_size = 8,8,2\ndwell = 100\npause = 1000','hanis')">
"""

file_line_end = '\\ncontrols = startstop, speed, step, looprock, zoom\\ncontrols_style = display:flex;flex-flow:row;\\nbuttons_style = flex:auto;margin:2px;cursor:pointer;\\nbottom_controls = toggle\\ntoggle_size = 8,8,2\\ndwell = 100\\npause = 1000\',\'hanis\')">\
  <div id="container">\
    <div id="hanis"></div>\
    <p>' + loop_description + '\n\
      HAniS developed by Tom Whittaker (<a href="http://www.ssec.wisc.edu/hanis/">http://www.ssec.wisc.edu/hanis/</a>)\
    </p>\
  </div>\
</body>\
</html>'

full_html = html_1 + file_str + file_line_end

f = open(index_path,'w')
f.write(full_html)
f.close()
