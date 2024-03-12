# -*- coding: utf-8 -*-
import cdsapi
import calendar

def download_era5_data(start_year, end_year):
    c = cdsapi.Client()  # 初始化CDS API客户端
    for year in range(start_year, end_year + 1):  # 遍历指定的年份范围
        for month in range(1, 13):  # 遍历每个月
            _, last_day = calendar.monthrange(year, month)  # 获取该月的最后一天
            days = [f"{day:02d}" for day in range(1, last_day + 1)]  # 根据每月的天数生成日期列表
            
            try:
                c.retrieve(
                    'reanalysis-era5-land',
                    {
                        'variable':'2m_temperature',
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

# 替换起始和结束年份以下载数据
download_era5_data(1981, 1999)