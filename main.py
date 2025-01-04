# Get the frankenstein book

def book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents.lower()

def split_to_words():
    words = book().split()
    return words

def word_count():
    return len(split_to_words())

def characters():
    characters = []
    words = book().split()
    for word in words:
        for character in word:
            characters.append(character)
    return characters

def character_count(): # Count the amount of characters function
    character_list = characters() # Every character from the book passed from the function characters()
    character_letter_list = []
    for chara in character_list:
        if chara.isalpha():
            character_letter_list.append(chara)
    character_dictionary = {char: 0 for char in character_letter_list}
    for char in character_letter_list:
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    
    return character_dictionary

def character_report():
    characters = character_count()
    for character in characters:
        count = characters[character]
        print(f"The {character} character was found {count} times")
    
def main():
    book()
    print(f"--beginning report of books/frankenstein.txt--")
    print(f"{word_count()} words found in the document\n")
    character_report()

    print(f"--End of report--")

main()