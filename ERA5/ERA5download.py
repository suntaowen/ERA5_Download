# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:11:15 2024

@author: dell
"""
import cdsapi
import calendar
import os

def download_era5_data(variable, year, month):
    
    current_directory = os.getcwd()
    directory = current_directory + "/download"
    os.chdir(directory)#下载路径
    
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
                'time': [
                    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',
                ],
                'area': [53.5, 73.5, 18, 135,],
                'format': 'netcdf',
            },
            f'2m_temperature_{year}_{month:02d}.nc'
        )
    except Exception as e:
        print(f"Error downloading data for {year}-{month:02d}: {e}")