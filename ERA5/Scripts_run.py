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

sys.path.append(current_directory)# 设置为ERA5download.py的路径
os.chdir(directory)

file_type = "*.py"  # 查找所有.py文件

# 获取工作路径中的所有py文件名
scripts = glob.glob(f"{file_type}")
print(scripts)

processes = [subprocess.Popen(['python', script]) for script in scripts]

time.sleep(1)

# 等待所有进程完成
for p in processes:
    print(f"{p}_ongoing")
    p.wait()
    print(f"{p}_succeed")

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