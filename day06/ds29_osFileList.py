# file : ds29_osFileList.py
# desc : 윈도우 파일 리스트

import os
import sys

fnameAry = []
folderName = 'C:\Sources/ds-and-algorithm'


for dirName,sybDirList,fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)
print(fnameAry)
print(f'파일 갯수는 {len(fnameAry)}개')

fnameAry.sort(reverse = True) # 역순 정렬
print(fnameAry)