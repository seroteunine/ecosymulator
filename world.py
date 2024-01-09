class World:
    def __init__(self, amount: int):
        self.amount = amount

    def update_simulation(self, timestep: int = 1):
        self.amount *= 1.5