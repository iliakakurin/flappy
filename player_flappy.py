class Player():
    def __init__(self, w, h, color):
        self.x = w // 10
        self.y = h // 2
        self.r = min(w, h) // 15
        self.color = color
