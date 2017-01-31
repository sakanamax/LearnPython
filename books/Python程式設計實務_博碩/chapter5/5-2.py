# -*- coding: utf-8 -*-
# 因為是學習 python, 所以用了很多 print() 來觀察
import os, shutil, glob
source_dir = "images/"
# 透過 os 模組來取得 / 目錄相關狀態
disk = os.statvfs("/")
print(disk)

# 目前可用空間計算
freespace = disk.f_bsize * disk.f_blocks
print(freespace)

# 透過 glob 模組來取得目前檔案, 以 list 型態存放
pngfiles = glob.glob(source_dir+"*.png")
jpgfiles = glob.glob(source_dir+"*.jpg")
giffiles = glob.glob(source_dir+"*.gif")
allfiles = pngfiles + jpgfiles + giffiles
print(allfiles)

allfilesize = 0
# allfilesize 型態是 int, 所以用 str轉型來顯示
print("allfilesize:  " + str(allfilesize))

# 使用 for 來計算目前檔案大小
for f in allfiles:
    allfilesize += os.path.getsize(f)
print("allfilesize:  " + str(allfilesize))

# 如果所有檔案大小 > 目前可用空間 顯示空間不足, 離開程式
if allfilesize > freespace:
    print("磁碟空間不足")
    exit(1)

# 設定輸出資料夾, 預設在該目錄下的 output
target_dir = source_dir + "output"
print("target_dir:  " + target_dir)

# 檢查 target_dir 是否存在, 存在就離開
if os.path.exists(target_dir):
    print("資料夾已存在")
    exit(1)

# 建立  target_dir
os.mkdir(target_dir)
imageno = 0

for f in allfiles:
    # split() 將字串根據指定字元切成 list
    # 這邊最主要要取出檔案名稱 filename
    print("---- loop start ----")
    dirname, filename = f.split('/')
    print(dirname)
    print(filename)
    # 使用 split() 切出檔案名稱還有副檔名
    mainname, extname = filename.split('.')
    print(mainname)
    print(extname)
    # 定義輸出的檔案名稱在 target_dir 下, 以 imageno 為序號加副檔名
    targetfile = target_dir + '/' + str(imageno) + '.' + extname
    print(targetfile)
    # 使用 shutil 複製檔案
    shutil.copyfile(f, targetfile)
    # 將 imageno 加1
    imageno += 1
    print("---- loop end ----")