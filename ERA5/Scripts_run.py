# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:23:04 2024

@author: dell
"""
import glob
import os
import sys
import subprocess
import time

current_directory = os.getcwd()
directory = current_directory + "/ERA5_download_scripts"
os.chdir(directory)
sys.path.append(current_directory)# 添加ERA5download.py的路径

file_type = "*.py"
scripts = glob.glob(f"{file_type}")# 获取工作路径中的所有py文件名

for script in scripts:
    print(script + '--ready!')

processes = [subprocess.Popen(['python', script]) for script in scripts]

time.sleep(1)

## 等待所有进程完成 ##
 for p in processes:
     print(f"{p}_ongoing")
     p.wait()
     print(f"{p}_succeed")

## debug代码 ##
# processes = []
# for script in scripts:
#     print(f"Running script: {script}")
#     proc = subprocess.Popen(['python', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     processes.append(proc)

# for p in processes:
#     stdout, stderr = p.communicate()

#     if stdout:
#         print("succeed:", stdout.decode())
#     if stderr:
#         print("error:", stderr.decode())
