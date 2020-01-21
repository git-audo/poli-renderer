
class Camera:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move(self, direction, delta=0.5):
        if direction == 'x':
            self.x += delta
        elif direction == 'y':
            self.y += delta
        elif direction == 'z':
            self.z += delta
