class World:
    def __init__(self, amount: int, dimension: (int, int)):
        self.dimension = dimension
        self.animals = [True] * amount

    def update_simulation(self, amount_of_updates: int = 1):
        for _ in range(amount_of_updates):
            self.animals *= 2
