# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:39:39 2024

@author: dell
"""
def Create_ERA5_land_download_script(kind, variable, start_year, end_year):
    
    for year in range(start_year, end_year + 1):  # 遍历指定的年份范围
    
        for month in range(1, 13):  # 遍历每个月

            filename = f'{kind}_{variable}_{year}_{month:02d}.py'
            
            code = f"""
import ERA5download as ed

ed.download_era5_land_data('{kind}', '{variable}', {year}, {month})
"""

            with open(filename, 'w') as file:
                # 将代码写入文件
                file.write(code)
        
            print(f"'{filename}' has been created and populated with code.")

def Create_ERA5_singlelevels_download_script(kind, variable, start_year, end_year):
    
    for year in range(start_year, end_year + 1):  # 遍历指定的年份范围
    
        filename = f'{kind}_{variable}_{year}.py'
        
        code = f"""
import ERA5download as ed

ed.download_era5_data_singlelevels('{kind}', '{variable}', {year})
"""

        with open(filename, 'w') as file:
            # 将代码写入文件
            file.write(code)
    
        print(f"'{filename}' has been created and populated with code.")
            
def Create_ERA5_pressurelevels_download_script(kind, variable, start_year, end_year):
    
    for year in range(start_year, end_year + 1):  # 遍历指定的年份范围
    
        filename = f'{kind}_{variable}_{year}.py'
        
        code = f"""
import ERA5download as ed

ed.download_era5_data_pressurelevels('{kind}', '{variable}', {year})
"""

        with open(filename, 'w') as file:
            # 将代码写入文件
            file.write(code)
    
        print(f"'{filename}' has been created and populated with code.")            


    