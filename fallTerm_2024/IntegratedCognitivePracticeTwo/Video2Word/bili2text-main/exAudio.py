import sys
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import os
import time


def flv_mp3(name, folder):
    # 构建视频和音频文件路径
    video_path = os.path.join(folder, f"{name}.mp4")
    audio_output_path = os.path.join("audio/conv", f"{name}.mp3")

    # 如果音频文件已存在，则跳过处理
    if os.path.exists(audio_output_path):
        print(f"音频文件已存在：{audio_output_path}")
        return audio_output_path

    # 确保视频文件存在
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"视频文件未找到：{video_path}")

    print(f"正在处理视频：{video_path}")
    clip = VideoFileClip(video_path)

    # 提取音频部分
    audio = clip.audio
    os.makedirs("audio/conv", exist_ok=True)
    audio.write_audiofile(audio_output_path)
    print(f"音频提取成功：{audio_output_path}")
    return audio_output_path


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python exAudio.py <视频文件名> <文件夹路径>")
        sys.exit(1)

    video_name = sys.argv[1]
    video_folder = sys.argv[2]

    try:
        audio_path = flv_mp3(video_name, video_folder)
        print(f"音频文件已保存：{audio_path}")
    except Exception as e:
        print(f"处理失败：{e}")
        sys.exit(1)
