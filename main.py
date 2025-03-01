import whisper
from datetime import datetime

def format_time(seconds):
    # 将秒转换为 HH:MM:SS 格式
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    sec = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{sec:06.3f}".replace(".", ",")  # 兼容srt格式

def main():
    model = whisper.load_model("small", device="cpu")
    
    result = model.transcribe(
        "demo.m4a",
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
