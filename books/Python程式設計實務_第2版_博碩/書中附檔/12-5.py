# -*- coding: utf-8 -*-
# 程式 12-5 (Python 3 Version)

import os, time, exifread, glob, sys, shutil

def get_year_month(fullpathname):
    fp = open(fullpathname, 'rb')
    exif = exifread.process_file(fp)
    ym = 0
    if 'EXIF DateTimeOriginal' in exif:
        ym = exif['EXIF DateTimeOriginal'].values
    else:
        ym = time.strftime('%Y:%m:%d', \
		time.localtime(os.stat(fullpathname).st_ctime))
    fp.close()
    return ym[0:4], ym[5:7]

if len(sys.argv)<2:
    print("Usage: python 12-6.py <source_dir>")
    exit()
source_dir = sys.argv[1]
if not os.path.exists('photos'):
    os.mkdir('photos')
allfiles = glob.glob(source_dir+'/*.jpg') + glob.glob(source_dir+'/*.png')

for imagefile in allfiles:
    filename = os.path.split(imagefile)[-1]
    y, m = get_year_month(imagefile)
    target_dir = os.path.join(os.path.join('photos', y ),m)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
    i=0
    ori_filename = filename
    while True:
        if not os.path.exists(os.path.join(target_dir,filename)):
            print("target:{}".format(filename))
            shutil.copy(imagefile, os.path.join(target_dir,filename))
            break
        else:
            ext = os.path.splitext(ori_filename)[-1]
            filename = "{}-{}{}".format(os.path.splitext(ori_filename)[0] \
				,str(i), ext)
            i = i + 1
