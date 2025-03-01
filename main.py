from webdav3.client import Client

# 配置 WebDAV 连接
options = {
    'webdav_hostname': "https://chogo.teracloud.jp/dav/",
    'webdav_login':    "ThomasXie",
    'webdav_password': "43rKo29cev5Uzbyp",
    # 'webdav_root':     "/files/"  # 服务器根路径（根据实际情况调整）
}

client = Client(options)

# # 示例1: 上传文件
# local_file = r"E:\学习\高中\网课\生物\高一下\output.mp3"
remote_path = "/documents/output.mp3"
# try:
#     client.upload(remote_path, local_file)
#     print(f"上传成功: {local_file} -> {remote_path}")
# except Exception as e:
#     print(f"上传失败: {str(e)}")

# 示例2: 下载文件
downloaded_file = "output.mp3"
try:
    client.download(remote_path, downloaded_file)
    print(f"下载成功: {remote_path} -> {downloaded_file}")
except Exception as e:
    print(f"下载失败: {str(e)}")

# # 示例3: 创建目录
# new_dir = "/documents"
# try:
#     client.mkdir(new_dir)
#     print(f"目录创建成功: {new_dir}")
# except Exception as e:
#     print(f"目录创建失败: {str(e)}")

# 示例4: 列出文件
# try:
#     file_list = client.list("/documents")
#     print("目录内容:")
#     for item in file_list:
#         print(f" - {item}")
# except Exception as e:
#     print(f"列表获取失败: {str(e)}")

# 示例5: 删除文件
# try:
#     client.clean(remote_path)  # 删除文件
#     # client.clean(new_dir)    # 删除空目录
#     print(f"删除成功: {remote_path}")
# except Exception as e:
#     print(f"删除失败: {str(e)}")
