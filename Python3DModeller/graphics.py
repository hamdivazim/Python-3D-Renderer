import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera

class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        # Setup window
        pg.init()
        pg.display.set_caption('OpenGL Lab | codingboy_CW')
        self.WIN_SIZE = win_size

        # Set OpenGL attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        # Create OpenGL context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        # Detect and use existing OpenGl Context
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST)

        # Create an object to track time
        self.clock = pg.time.Clock()

        # Camera
        self.camera = Camera(self)

        # Scene
        self.scene = Cube(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # Clear framebuffer
        self.ctx.clear(color=(0.08,0.16,0.18))

        # Render scene
        self.scene.render()

        # Swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.render()
            self.clock.tick(60)