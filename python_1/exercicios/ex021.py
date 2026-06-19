# Exercicio 021
# Faça um programa que abra e reproduza o áudio de um arquivo MP3

import miniaudio
import time

stream = miniaudio.stream_file('audio_exemplo.mp3')
device = miniaudio.PlaybackDevice()
device.start(stream)

time.sleep(stream.duration)
device.close()