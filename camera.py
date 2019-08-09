
class Camera:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def forward(self):
        self.z += 2

    def backward(self):
        self.z -= 2

    def left(self):
        self.x -= 0.5

    def right(self):
        self.x += 0.5

    def up(self):
        self.y += 0.5

    def down(self):
        self.y -= 0.5

