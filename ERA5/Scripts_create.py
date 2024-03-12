# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:13:20 2024

@author: dell
"""

import Create_ERA5_download_script as ce
import os
import glob

# 获取当前工作目录的绝对路径并指定工作路径
current_directory = os.getcwd()
directory = current_directory + "/ERA5_download_scripts"
os.chdir(directory)

## 以下三种参数需要设置 ##

kind = 'pressurelevels' #例 kind = 'land'  'singlelevels' 'pressurelevels'只能选一个

#例 variable_list = ["2m_temperature", "forecast_albedo", "surface_pressure"] ['total_column_ozone', 'total_column_water_vapour']
variable_list = ['relative_humidity']#选择自己所需要下载的参数，可选多个下载

start_year = 1983
end_year = 1985

## 删除曾经的.py文件 ##
file_type = "*.py"
files_to_delete = glob.glob(file_type)

if files_to_delete == []:
    True
else:
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Deleted {file}")
        except OSError as e:
            print(f"Error: {file} : {e.strerror}")

# 创建脚本文件
for variable in variable_list:
    
    if kind == 'land':
        ce.Create_ERA5_land_download_script(kind, variable, start_year, end_year)
        
    elif kind == 'singlelevels':
        ce.Create_ERA5_singlelevels_download_script(kind, variable, start_year, end_year)
        
    elif kind == 'pressurelevels':
        ce.Create_ERA5_pressurelevels_download_script(kind, variable, start_year, end_year)
        
    else:
        print("Kind error!")
    


