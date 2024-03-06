# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:39:39 2024

@author: dell
"""
def Created_ERA5_download_script(variable, start_year, end_year):
    
    for year in range(start_year, end_year + 1):  # 遍历指定的年份范围
    
        for month in range(1, 13):  # 遍历每个月

            filename = f'{variable}_{year}_{month:02d}.py'
            
            code = f"""
import ERA5download as ed

ed.download_era5_data('{variable}', {year}, {month})
"""

            with open(filename, 'w') as file:
                # 将代码写入文件
                file.write(code)
        
            print(f"'{filename}' has been created and populated with code.")
            
            
            

    
    