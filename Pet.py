class Pet:
    def __init__(self):
        self.name = "Max"  # Set the pet's name to Max
        self.hunger = 5  # Default hunger level
        self.energy = 5  # Default energy level
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger, but not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy, but not above 10

    def play(self):
        if self.energy >= 2:  # Ensure enough energy to play
            self.energy -= 2  # Decrease energy
            self.happiness = min(10, self.happiness + 2)  # Increase happiness
            self.hunger = min(10, self.hunger + 1)  # Increase hunger
        else:
            print(f"{self.name} is too tired to play. Let them rest first!")

    def get_status(self):
        print(f"Pet Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)  # Add trick to the list
        self.happiness = min(10, self.happiness + 1)  # Increase happiness
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

my_pet = Pet()

# Interactive demonstration
while True:
    print("\nChoose an action:")
    print("1. Eat")
    print("2. Sleep")
    print("3. Play")
    print("4. Get Status")
    print("5. Train a Trick")
    print("6. Show Tricks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        my_pet.eat()
    elif choice == "2":
        my_pet.sleep()
    elif choice == "3":
        my_pet.play()
    elif choice == "4":
        my_pet.get_status()
    elif choice == "5":
        trick = input("What trick would you like to teach Max? ")
        my_pet.train(trick)
    elif choice == "6":
        my_pet.show_tricks()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
