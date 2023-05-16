#视频码率计算器
print("欢迎使用视频码率计算器")

#获取视频总长度（单位为秒）
hours=int(input("视频时长为（小时）:"))
mins=int(input("视频时长为（分钟）:"))
seconds=int(input("视频时长为（秒）:"))
total_seconds=hours*3600+mins*60+seconds

#获取视频总大小（单位为MB）
size=int(input("视频文件大小为(MB):"))

#计算码率（单位为Mbps）
bitrate=size*8/total_seconds

#输出结果
print(f"该视频码率大小为 {round(bitrate,2)} Mbps:")