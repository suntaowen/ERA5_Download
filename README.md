 ## ERA5_Download ##
 多线程批量下载ERA5_land数据（已更新singlelevels和pressurelevels类型数据的下载）

 首先根据需要修改Script_create.py中的kind和variable_list参数 例如ERA5_Land数据就将kind设置为land（唯一），下载两米温度就在variable_list中添加2m_temperature参数（可添加多个），
 然后根据需要修改ERA5download.py中的![屏幕截图 2024-03-13 215342](https://github.com/suntaowen/ERA5_Download/assets/146147840/b8517017-9eac-483e-adf9-79e9b0334801)等参数。

 ## 开始执行 ##
 运行Scripts_create.py会创建下载ERA5数据的多个并行脚本并存放在ERA5_download_scripts文件夹中。

 脚本建立完成之后运行Scripts_run.py即可执行Scripts_create.py创建的并行脚本。
 
 下载的数据文件会放置在..\ERA5_download_scripts\download文件夹中。
