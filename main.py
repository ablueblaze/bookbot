def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    count = word_count(text)
    letters = letter_count(text)
    list_of_letters = convert_to_list(letters)
    sorted_letters = sorted(list_of_letters, reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print("")

    for c in sorted_letters:
        print(f"The {c['character']} character was found {c['num']} times")
    
    print("--- End report ---")


# Returns the text of the given file
def get_text(book_path):
    with open(book_path) as f:
        return f.read()


# Returns the number of words
def word_count(text):
    return len(text.split())


# Returns the number of times each letter apears in the given text
# Format is in a dictionary
def letter_count(text):
    lowered_string = text.lower()
    character_count_dict = {}

    for character in lowered_string:
        if character in character_count_dict and character.isalpha():
            character_count_dict[character] += 1
        elif character.isalpha():
            character_count_dict[character] = 1
        else:
            pass
    return character_count_dict


# Used to sort the letters by the num key
def sort_on(dict):
    return dict['num']


# ----COMPLETE----
# Return a list of dictionaries that
def convert_to_list(letter_dict):
    list_of_dictionaries = []

    # convert the dictionary into a list of dictionaries
    for key in letter_dict:
        list_of_dictionaries.append({"character": key, "num": letter_dict[key]})

    return list_of_dictionaries


main()

