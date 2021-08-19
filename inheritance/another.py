class Bubi():
    def __init__(self):
        self.x = 5


class Cyfra(Bubi):
    def __init__(self):
        self.y = 5
        super().__init__()

    def add(self):
        self.x += 1


cyfra = Cyfra()

cyfra.add()
y = cyfra.x

print(y)