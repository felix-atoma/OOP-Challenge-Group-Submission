class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        print(f"{self.name} is eating... 🍖")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.name} is sleeping... 😴")
        self.energy = min(10, self.energy + 5)

    def play(self):
        print(f"{self.name} is playing... 🐾")
        if self.energy <= 0:
            print(f"{self.name} is too tired to play!")
        else:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger} 🍗")
        print(f"Energy: {self.energy} 🔋")
        print(f"Happiness: {self.happiness} 😊")
        print(f"Tricks: {self.tricks if self.tricks else 'None yet!'}\n")

    def train(self, trick):
        print(f"{self.name} is learning a new trick: {trick} 🎓")
        self.tricks.append(trick)

    def show_tricks(self):
        print(f"{self.name} knows the following tricks:")
        for trick in self.tricks:
            print(f" - {trick}")