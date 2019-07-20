import time
import pyglet


a = input("enter the hour you want to weak up: ")
b = input("enter the minute you want to weak up: ")

while True:
    now = time.localtime()
    if now.tm_hour == int(a) and now.tm_min == int(b):
        print("weak up")
        music = pyglet.resource.media('WAV_1MG.wav')
        music.play()
        pyglet.app.run()
        break
    else:
        print("sleep")
        
