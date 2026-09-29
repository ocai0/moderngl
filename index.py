import moderngl
import moderngl_window as mglw
import numpy as np
class Application(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "Primeiro triângulo"
    window_size = (800, 600)
    aspect_ratio = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.programa = self.ctx.program(
        vertex_shader="""
            #version 330
            in vec2 in_pos;
            void main() {
            gl_Position = vec4(in_pos, 0.0, 1.0);
            }
        """,
        fragment_shader="""
            #version 330
            out vec4 fragColor;
            void main() {
            fragColor = vec4(1.0, 0.5, 0.1, 1.0);
            }
        """
        )
        vertices = np.array([
            -0.6, -0.5,
            0.6, -0.5,
            0.0, 0.6
        ], dtype="f4")
        self.vbo = self.ctx.buffer(vertices.tobytes())
        self.vao = self.ctx.vertex_array(
            self.programa,
            [
                (
                    self.vbo,
                    "2f",
                    "in_pos"
                )
            ]
        )
    def on_render(self, tempo, intervalo):
        self.ctx.clear(0.08, 0.10, 0.15)
        self.vao.render(mode=moderngl.TRIANGLES)

    def on_key_event(self, tecla, acao, modificadores):
        keys = self.wnd.keys
        if acao == keys.ACTION_PRESS:
            if tecla == keys.SPACE:
                if self.ctx.wireframe == True: self.ctx.wireframe = False
                else: self.ctx.wireframe = True
                
mglw.run_window_config(Application)