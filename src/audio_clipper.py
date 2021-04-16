import moviepy.editor as mp
import librosa
import IPython.display as ipd
from pydub import AudioSegment
import os
from os import path
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

print(os.getcwd())

my_clip = mp.VideoFileClip(r"test.mp4")
data = my_clip.audio.write_audiofile(r"test_mp3.mp3")
# convert wav from mp3

# sound = AudioSegment.from_mp3(r"C:\Users\mgupta\Desktop\SEL Project\ASELI\test_mp3.mp3")
# sound.export('test.wav', format="wav")

# Total length in seconds for test audio = 7:16 = 436 seconds


def clip(audio):
    for i in range(0, 436, 15):
        file = ffmpeg_extract_subclip(audio, i, i + 15)
        i = i + 15
        yield file


s = clip("test.wav.wav")
type(s)
