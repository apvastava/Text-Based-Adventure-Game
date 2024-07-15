import time

def intro():
    print("Welcome to the Text Adventure Game!")
    time.sleep(2)
    print("You find yourself standing in front of a mysterious cave...")
    time.sleep(2)
    print("Your mission is to explore the cave and find the hidden treasure!")
    time.sleep(2)

def choose_cave():
    print("\nYou must choose a cave to enter:")
    time.sleep(1)
    print("1. Cave 1")
    time.sleep(1)
    print("2. Cave 2")
    time.sleep(1)
    return input("Which cave will you enter? (1 or 2): ")

def explore_cave(cave):
    print(f"\nYou enter cave {cave}...")
    time.sleep(2)
    print("It's dark and spooky...")
    time.sleep(2)
    print("You cautiously move forward...")
    time.sleep(2)

    chosen_cave = int(cave)

    if chosen_cave == 1:
        print("You encounter a giant spider!")
        time.sleep(2)
        print("You fight bravely and defeat the spider!")
        time.sleep(2)
        print("You find a chest full of gold!")
    else:
        print("You encounter a pack of hungry wolves!")
        time.sleep(2)
        print("You manage to escape, but you're injured.")
        time.sleep(2)
        print("You find a small pouch with some coins.")

def play_game():
    intro()
    cave_choice = choose_cave()
    explore_cave(cave_choice)

if __name__ == "__main__":
    play_game()
