# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:13:20 2024

@author: dell
"""

import Created_ERA5_download_script as ce
import os

# 获取当前工作目录的绝对路径并指定工作路径
current_directory = os.getcwd()
directory = current_directory + "/ERA5_download_scripts"
os.chdir(directory)

#例 variable_list = ["2m_temperature", "forecast_albedo", "surface_pressure"]

variable_list = ["2m_temperature"]#选择自己所需要下载的参数，可同时多个下载

# 创建脚本文件
for variable in variable_list:
    ce.Created_ERA5_download_script(variable, 1981, 1981)


