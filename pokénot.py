# Aiden Canady
# 11/26/2024
# P5HW
# Using functions to create a game

import random
characters = []

def createCharacter():
    print("Create Your Character!")
    
    # Get inputs for character attributes
    name = input("Enter the character's name: ")
    health = int(input("Enter the character's health (rec. 300 > your health > 100): "))
    attack = int(input("Enter the character's attack value (e.g., 50): "))
    defense = int(input("Enter the character's defense value (e.g., 45): "))
    speed = int(input("Enter the character's speed value (e.g., 30): "))

    # Define valid types
    valid_types = ["fire", "water", "plant", "earth", "wind"]
    char_type = input("Enter the character's type (fire, water, plant, earth, wind): ").lower()
    
    # Validate the type input
    if char_type not in valid_types:
        print(f"Invalid type! Defaulting to 'fire'.")
        char_type = "fire"
    
    # Create the dictionary to hold character attributes
    character = {
        "name": name,
        "health": health,
        "attack": attack,
        "defense": defense,
        "speed": speed,
        "type": char_type,
    }
    
    return character

def display_character(character):
    """
    Displays the character's information in a neat format.
    
    Args:
        character (dict): A dictionary containing the character's attributes.
    """
    print("\n--- Character Information ---")
    name_or_type = character.get("name", character.get("type", "Unknown"))
    print(f"Name: {name_or_type}")
    print(f"Health: {character['health']}")
    print(f"Attack: {character['attack']}")
    print(f"Defense: {character['defense']}")
    print(f"Speed: {character['speed']}")
    print(f"Type: {character['type']}")
    print("-----------------------------")

def enemy():
    global characters
    """
    Creates a random enemy with a type and randomly generated stats.

    Returns:
        dict: A dictionary containing the enemy's type and stats.
    """
    # List of potential enemy types
    enemy_types = ["Goblin", "Skeleton", "Ghost", "Orc", "Zombie", "Troll"]
    
    # Randomly choose an enemy type
    enemy_type = random.choice(enemy_types)
    
    # Generate random stats between 1 and 200
    health = random.randint(1, 300)
    attack = random.randint(1, 200)
    defense = random.randint(1, 100)
    speed = random.randint(1, 200)
    
    # Create the enemy dictionary
    enemy_character = {
        "type": enemy_type,
        "health": health,
        "attack": attack,
        "defense": defense,
        "speed": speed,
    }
    
    return enemy_character

def select_character():
    """
    Allows the user to select a character from the list of created characters.

    Returns:
        dict: The selected character dictionary.
    """
    if not characters:
        print("\nNo characters available. Please create a character first.")
        return None

    print("\n--- Choose Your Character ---")
    for idx, char in enumerate(characters, start=1):
        print(f"{idx}. {char['name']}")

    while True:
        try:
            choice = int(input("Enter the number of the character you want to use: "))
            if 1 <= choice <= len(characters):
                return characters[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def battle():
    """
    Executes a battle between a user-selected character and a randomly generated enemy.
    The battle ends when either combatant's health reaches 0.
    """
    global characters
    print("\n--- Battle Start ---")
    
    # Select user's character
    user_character = select_character()
    if user_character is None:
        return  # Exit if no character is available
    
    # Generate a random enemy
    opponent = enemy()
    
    # Display stats
    print("\nYour Character:")
    display_character(user_character)
    print("\nOpponent:")
    display_character(opponent)
    
    # Battle loop
    while user_character['health'] > 0 and opponent['health'] > 0:
        print("\n--- Battle Round ---")
        
        # User character attacks opponent
        if user_character['attack'] > opponent['defense']:
            damage_to_opponent = max(1, int(opponent['defense'] * random.uniform(1.1,1.6)))
        elif user_character['attack'] < opponent['defense']:
            damage_to_opponent = max(1, int(opponent['defense'] * random.uniform(0.6,0.9)))
        else:
            damage_to_opponent = max(1, opponent['defense'])  # Flat value

        opponent['health'] -= damage_to_opponent
        print(f"{user_character['name']} attacks {opponent['type']} for {damage_to_opponent} damage!")
        
        # Check if opponent is defeated
        if opponent['health'] <= 0:
            print(f"\n{opponent['type']} has been defeated! You win!")
            break
        
        # Opponent attacks user character
        if opponent['attack'] > user_character['defense']:
            damage_to_user = max(1, int(user_character['defense'] * random.uniform(1.1,1.6)))
        elif opponent['attack'] < user_character['defense']:
            damage_to_user = max(1, int(user_character['defense'] * random.uniform(0.6,0.9)))
        else:
            damage_to_user = max(1, user_character['defense'])  # Flat value

        user_character['health'] -= damage_to_user
        print(f"{opponent['type']} attacks {user_character['name']} for {damage_to_user} damage!")
        
        # Check if user character is defeated
        if user_character['health'] <= 0:
            print(f"\n{user_character['name']} has been defeated! You lose!")
            break

    print("\n--- Battle End ---")


    
def main_menu():
    global characters
    """
    Displays the main menu and allows the user to interact with options:
    - Create Character
    - List of Characters
    - Battle
    """
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Character")
        print("2. List of Characters")
        print("3. Battle")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Create a new character
            new_character = createCharacter()
            characters.append(new_character)
            print("\nCharacter created successfully!")
        
        elif choice == "2":
            # List all characters
            if not characters:
                print("\nNo characters have been created yet.")
            else:
                print("\n--- List of Characters ---")
                for idx, character in enumerate(characters, start=1):
                    print(f"\nCharacter {idx}:")
                    display_character(character)
        
        elif choice == "3":
            # Placeholder for Battle functionality
            battle()
        
        elif choice == "4":
            # Exit the menu
            print("\nExiting the game. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please select a valid option.")

def main():
    print("game initiated")
    main_menu()
    
if __name__ == "__main__":
    main()
