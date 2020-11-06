class BlackBox:
    def __init__(self):
        self.C = rand.randint(100)
    def check(self, guess):
        return (guess - self.C) / abs(guess - self.C)