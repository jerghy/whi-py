import whisper
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth

mp3name="output.mp3"
url = "https://chogo.teracloud.jp/dav/documents/"+mp3name
auth = HTTPBasicAuth("ThomasXie", "43rKo29cev5Uzbyp")

response = requests.get(url, auth=auth)
if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
        print("下载成功")
else:
    print(f"下载失败，状态码：{response.status_code}")



def format_time(seconds):
    # 将秒转换为 HH:MM:SS 格式
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    sec = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{sec:06.3f}".replace(".", ",")  # 兼容srt格式

def shangchun(name):
    # 配置参数
    webdav_host = "https://chogo.teracloud.jp/dav/"
    remote_path = "/output/"+name+".txt"  # 远程路径
    local_file = "result.txt"  # 本地文件路径
    username = "ThomasXie"
    password = "43rKo29cev5Uzbyp"
    
    # 构造完整 URL
    url = webdav_host.rstrip('/') + remote_path
    auth = HTTPBasicAuth(username, password)
    
    try:
        with open(local_file, 'rb') as file:
            response = requests.put(url, data=file, auth=auth)
        
        if response.status_code in (200, 201, 204):
            print(f"上传成功: {local_file} -> {remote_path}")
        else:
            print(f"上传失败，HTTP 状态码: {response.status_code}")
    
    except Exception as e:
        print(f"上传异常: {str(e)}")

def main():
    model = whisper.load_model("large", device="cpu")
    
    result = model.transcribe(
        "output.mp3",
        language="zh",
        fp16=False,
        verbose=False
    )
    
    with open("result.txt", "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            start = format_time(segment["start"])
            end = format_time(segment["end"])
            f.write(f"[{start} --> {end}] {segment['text'].strip()}\n\n")
    
    print("转换完成！")

    shangchun(mp3name.split(".")[0])

if __name__ == "__main__":
    main()
