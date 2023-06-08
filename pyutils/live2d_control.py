from gtts import gTTS
import librosa
import time
import pygame
import numpy as np



def my_tts(text, save_path):
    tts = gTTS(text, lang="zh-CN")
    tts.save(save_path)


def tts_and_play_audio(text):
    tmp_audio_path = 'tmp.mp3'
    my_tts(text, tmp_audio_path)
    pygame.mixer.init()
    pygame.mixer.music.load(tmp_audio_path)  
    pygame.mixer.music.set_volume(0.8) 

    x , sr = librosa.load(tmp_audio_path, sr=8000)

    x = x  - min(x)
    x = x  / max(x)
    x= np.log(x) + 1
    x = x  / max(x) * 1.2

    pygame.mixer.music.play()
    s_time = time.time()
    try:
        for _ in range(int(len(x) / 800)):
            it = x[int((time.time() - s_time) * 8000)+1]
            # print(it)
            if it < 0:
                it = 0
            with open("tmp.txt", "w") as f:
                f.write(str(float(it)))
            time.sleep(0.1)
    except:
        pass

    time.sleep(0.1)
    with open("tmp.txt", "w") as f:
        f.write("0")
