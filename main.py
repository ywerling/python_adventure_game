import time

# Define the player character
class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.inventory = []

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up! Now at level {self.level}.")

# Define the mentor character
class Mentor:
    def __init__(self, name="Archmage Pyra"):
        self.name = name

    def give_hint(self):
        hints = [
            "Remember, variables store values that you can use later.",
            "Use conditionals to make decisions in your code.",
            "Loops help you repeat actions multiple times efficiently.",
            "Functions can help organize your code and make it reusable."
        ]
        print(f"{self.name} says: {hints[player.level - 1]}")

# Define a basic quest
def enchanted_forest():
    print("\nWelcome to the Enchanted Forest!")
    print("Your first task is to count and organize magical herbs.")
    herbs = 10
    basket = 5
    total_herbs = herbs + basket
    print("Total herbs:", total_herbs)
    print("Congratulations! You've completed the Enchanted Forest quest.\n")
    player.xp += 10
    player.level_up()

def arcane_library():
    print("\nWelcome to the Arcane Library!")
    print("Your task is to organize books using conditionals.")
    password = input("Enter the password to unlock the library: ")
    if password == "open_sesame":
        print("The door opens.")
        print("Congratulations! You've completed the Arcane Library quest.\n")
        player.xp += 20
        player.level_up()
    else:
        print("The door remains closed. Try again.\n")
        arcane_library()

def crystal_caves():
    print("\nWelcome to the Crystal Caves!")
    print("Your task is to collect magical crystals using loops.")
    crystals = ["red", "blue", "green"]
    for crystal in crystals:
        print("Collected a", crystal, "crystal.")
    print("Congratulations! You've completed the Crystal Caves quest.\n")
    player.xp += 30
    player.level_up()

def dragons_lair():
    print("\nWelcome to the Dragon's Lair!")
    print("Your task is to use functions to create a healing spell.")
    def heal(creature):
        print(f"{creature} is healed!")

    creature = "Unicorn"
    heal(creature)
    print("Congratulations! You've completed the Dragon's Lair quest.\n")
    player.xp += 40
    player.level_up()

def dark_tower():
    print("\nWelcome to the Dark Tower!")
    print("Your final task is to combine all your skills to defeat Malakar the Corrupt.")
    def attack(enemy):
        print(f"Attacked {enemy} with a powerful spell!")

    if player.level >= 5:
        attack("Malakar the Corrupt")
        print("Congratulations! You've defeated Malakar and lifted the dark spell.\n")
    else:
        print("You need to be at least level 5 to face Malakar. Keep training!\n")

# Main game loop
def main():
    global player
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    mentor = Mentor()

    print(f"\nWelcome, {player.name}, to Code Quest!")
    time.sleep(1)

    while player.level < 5:
        mentor.give_hint()
        if player.level == 1:
            enchanted_forest()
        elif player.level == 2:
            arcane_library()
        elif player.level == 3:
            crystal_caves()
        elif player.level == 4:
            dragons_lair()

    dark_tower()

    print("Thank you for playing Code Quest!")

if __name__ == "__main__":
    main()
