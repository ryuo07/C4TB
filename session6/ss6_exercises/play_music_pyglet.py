import pyglet

music = pyglet.resource.media('WAV_1MG.wav')
music.play()

pyglet.app.run()