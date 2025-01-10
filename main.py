# Entry point
def main():
    # Relative path from current root
    path_to_file = "books/frankenstein.txt"
    # Access the book file
    text = get_text(path_to_file)
    # Total number of words
    words = get_count_words(text)
    # Number of chars
    chars = get_count_chars(text)
    sorted_list = get_char_to_list(chars)

    print(f"--- Begin report of {path_to_file} ---")
    # Print total words
    print(f"{words} words found in the document\n")
    # Sorts the amount of characters(alphabet) from highest to lowest
    for s in sorted_list:
        print(f"The '{s['char']}' character was found {s['num']} times")
       
    print("--- End report ---")

def get_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_count_words(text):
    words = text.split()
    return len(words)

def get_count_chars(text):
    char_list = {}
    lowered_string = text.lower()
    for s in lowered_string:
        if s in char_list:
            char_list[s] += 1
        else:
            char_list[s] = 1
    return char_list
# A function that takes a dictionary and returns the value of the "num" key
def sort_on(dict):
    return dict["num"]

def get_char_to_list(chars):
    sorted_list = []
    for c in chars:
        if c.isalpha():
            sorted_list.append({"char": c, "num": chars[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
# Calls the main method
main()


