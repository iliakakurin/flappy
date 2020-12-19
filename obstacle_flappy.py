import random
class Obstacle():
    def __init__(self, w_screen, h_screen, color):
        self.x = (9 * w_screen) // 10
        self.w = random.randint(10, w_screen // 20)
        self.h = random.randint(10, 3 * h_screen // 4)
        self.gap = random.randint(min(w_screen, h_screen) // 15 * 4, min(w_screen, h_screen) // 15 * 10)
        self.color = color
