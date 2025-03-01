import whisper
from datetime import datetime
from webdav3.client import Client

# 配置 WebDAV 连接
options = {
    'webdav_hostname': "https://chogo.teracloud.jp/dav/",
    'webdav_login':    "ThomasXie",
    'webdav_password': "43rKo29cev5Uzbyp",
    # 'webdav_root':     "/files/"  # 服务器根路径（根据实际情况调整）
}

client = Client(options)
remote_path = "/documents/output.mp3"
downloaded_file = "output.mp3"
try:
    client.download(remote_path, downloaded_file)
    print(f"下载成功: {remote_path} -> {downloaded_file}")
except Exception as e:
    print(f"下载失败: {str(e)}")



def format_time(seconds):
    # 将秒转换为 HH:MM:SS 格式
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    sec = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{sec:06.3f}".replace(".", ",")  # 兼容srt格式

def main():
    model = whisper.load_model("small", device="cpu")
    
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

if __name__ == "__main__":
    main()
