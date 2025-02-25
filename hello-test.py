import pyglet
window = pyglet.window.Window(width=800, height=500)
label = pyglet.text.Label('Hello, Audra', font_size=100, x=250, y=100)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()


