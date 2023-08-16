import random

# Create a dictionary to assign values to each letter
# Use this dictionary to calculate the total value of a word

# Create a list of the characters in the English alphabet
# Use the random library in some way to assign letters to a player's hand

# Create a list of alphabet letters which reflects the provided distribution
# Use the random library again

# Read through the dictionary.txt file, and turn it into a list of words
# For each word in the dictionary, I will check if the count of each letter in the dictionary word
# is less than or equal to the count of this letter in 

points = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}


alphabet = "abcdefghijklmnopqrstuvwxyz"


tiles_distribution = {
    "a": 9,
    "b": 2,
    "c": 2,
    "d": 4,
    "e": 12,
    "f": 2,
    "g": 3,
    "h": 2,
    "i": 9,
    "j": 1,
    "k": 1,
    "l": 4,
    "m": 2,
    "n": 6,
    "o": 8,
    "p": 2,
    "q": 1,
    "r": 6,
    "s": 4,
    "t": 6,
    "u": 4,
    "v": 2,
    "w": 2,
    "x": 1,
    "y": 2,
    "z": 1,
}


def calculate_points_for_word(word: str):
    word = word.lower()
    word_points = 0
    for char in word:
        word_points += points[char]
    return word_points


def assign_seven_tiles_from_alphabet(tile_bag: str):

    player_hand = random.sample(tile_bag, 7)

    return player_hand


def create_tiles_bag(tiles_distribution: dict):

    list_of_tiles = []

    for key in tiles_distribution:

        list_of_tiles.append([key] * tiles_distribution[key])
    
    separated_list_of_tiles = []
    
    for char_list in list_of_tiles:

        for char in char_list:

            separated_list_of_tiles.append(char)
    
    return separated_list_of_tiles


# def assign_seven_tiles_from_tile_bag(tile_bag: list):


def find_valid_word(player_hand):

    print(player_hand)

    with open("dictionary.txt") as f:

        lines = f.read()
        lines = lines.split("\n")

    for word in lines:

        valid = True

        for char in word:

            if word.count(char) > player_hand.count(char):
                
                valid = False
                break
            
        if valid:
                
            return word
    
    return None


tile_bag = create_tiles_bag(tiles_distribution)

player_hand = assign_seven_tiles_from_alphabet(tile_bag)

print(find_valid_word(player_hand))