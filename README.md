 ## ERA5_Download ##
 多线程批量下载ERA5_land数据（已更新singlelevels和pressurelevels类型数据的下载）

 首先根据需要修改Script_create.py中的kind和variable_list参数 例如ERA5_Land数据就将kind设置为land（唯一），下载两米温度就在variable_list中添加2m_temperature参数（可添加多个），
 然后根据需要修改ERA5download.py中的参数。
 
 product_type_parameter,
 format_parameter,
 month_parameter,
 day_parameter,
 time_parameter,
 area_parameter,

 ## 开始执行 ##
 运行Scripts_create.py会创建下载ERA5数据的多个并行脚本并存放在ERA5_download_scripts文件夹中。

 脚本建立完成之后运行Scripts_run.py即可执行Scripts_create.py创建的并行脚本。
 
 下载的数据文件会放置在..\ERA5_download_scripts\download文件夹中。
 
 ## 注意 ##
 CDS API key需自己导入;
 
 ERA5_Land数据为逐年逐月下载其它数据均为逐年下载;

 目前该代码还有许多不完善的地方请不要随意传播，如有疑问随便问，我会尽快解决。

 如果运行Scripts_run.py出现问题请切换该代码中的debug代码

 
