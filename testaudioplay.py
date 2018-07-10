from pygame import mixer # Load the required library
import time

mixer.init()
mixer.music.load('audio/0.wav')
mixer.music.play()
time.sleep(2)
