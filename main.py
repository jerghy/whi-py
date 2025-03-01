import whisper
import os

def main():
    # 初始化模型
    model = whisper.load_model("small", device="cpu")
    
    # 执行语音识别
    result = model.transcribe(
        "demo.m4a",
        language="zh",
        fp16=False,
        verbose=False  # 在CI中关闭详细输出
    )
    
    # 保存结果
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print("转换完成！")

if __name__ == "__main__":
    main()
