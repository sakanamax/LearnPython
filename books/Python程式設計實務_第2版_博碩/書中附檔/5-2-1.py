#coding=utf-8
import os, shutil, glob, wmi
source_dir = "images"
import wmi
c = wmi.WMI()
disk = c.Win32_LogicalDisk()[0]
free_space = int(disk.freeSpace)
png_files = glob.glob(os.path.join(source_dir,"*.png"))
jpg_files = glob.glob(os.path.join(source_dir,"*.jpg"))
gif_files = glob.glob(os.path.join(source_dir,"*.gif"))
all_files = png_files + jpg_files + gif_files

all_file_size = 0
#以下的程式碼用來加總所有檔案使用的檔案大小
for f in all_files:
    all_file_size += os.path.getsize(f)

if all_file_size>free_space:
    print("磁碟空間不足")
    exit(1)

#以下的程式碼用來避免使用到重複的output資料夾
target_dir = os.path.join(source_dir,"output")
if os.path.exists(target_dir):
    no=1
    target_dir = os.path.join(source_dir, "output"+str(no))
    while os.path.exists(target_dir):
        no += 1
        target_dir = os.path.join(source_dir, "output"+str(no))
        
os.mkdir(target_dir)
imageno = 0

for f in all_files:
    dirname, filename = os.path.split(f)
    _, extname = os.path.splitext(filename)
    targetfile = os.path.join(target_dir,str(imageno)+extname)
    shutil.copyfile(f, targetfile)
    print("{}=>{}".format(f, targetfile))
    imageno += 1
