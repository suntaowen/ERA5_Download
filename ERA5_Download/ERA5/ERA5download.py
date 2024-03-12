# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:11:15 2024

@author: dell
"""
import cdsapi
import calendar
import os

## 下载路径 ##
current_directory = os.getcwd()
directory = current_directory + "/download"
os.chdir(directory)

## 参数调整 ##
pressure_levels_parameter = ['1000']

product_type_parameter = 'reanalysis'

format_parameter = 'netcdf'

time_parameter = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                  '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                  '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                  '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',]

area_parameter = [53.5, 73.5, 18, 135,]

day_parameter = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                 '31',]

month_parameter = ['01', '02', '03', '04', '05', '06',
                   '07', '08', '09', '10', '11', '12',]

ERA5_parameter_dictionary = {
                'product_type': product_type_parameter,
                'format': format_parameter,
                'month': month_parameter,
                'day': day_parameter,
                'time': time_parameter,
                'area': area_parameter,}

def download_era5_land_data(kind, variable, year, month):
    
    c = cdsapi.Client()

    _, last_day = calendar.monthrange(year, month)
    days = [f"{day:02d}" for day in range(1, last_day + 1)]
    
    try:
        c.retrieve(
            'reanalysis-era5-land',
            {
                'variable':f'{variable}',
                'year': str(year),
                'month': f'{month:02d}',
                'day': days,
                'time': time_parameter,
                'area': area_parameter,
                'format': format_parameter,
            },
            f'{kind}_{variable}_{year}_{month:02d}.nc')
        
    except Exception as e:
        print(f"Error downloading data for {year}-{month:02d}: {e}")
        
def download_era5_data_singlelevels(kind, variable, year, month = None):
    
    c = cdsapi.Client()
    try:
        c.retrieve(
            'reanalysis-era5-single-levels',
            {**{
                'variable': f'{variable}',
                'year': str(year),
                
                **ERA5_parameter_dictionary
            }},
            f'{kind}_{variable}_{year}.nc')
        
    except Exception as e:
        print(f"Error downloading data for {year}-{month:02d}: {e}")
        
def download_era5_data_pressurelevels(kind, variable, year, month = None):
    
    c = cdsapi.Client()
    try:
        c.retrieve(
            'reanalysis-era5-pressure-levels',
            {**{
                'variable': f'{variable}',
                'year': str(year),
                'pressure_level': pressure_levels_parameter,
                
                **ERA5_parameter_dictionary
            }},
            f'{kind}_{variable}_{year}.nc')
        
    except Exception as e:
        print(f"Error downloading data for {year}-{month:02d}: {e}")
        
        