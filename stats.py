# Return the number of each word appears in the string.
def get_num_words(text):
    return len(text.split())
# Return the number of each character appears in the string.
def get_num_chars(text):
    char_dict = {} # key is a string, value is an integer
    for char in text.lower(): # convert each character to lowercase to avoid duplicates
        if char not in char_dict:
            char_dict[char] = 1 # Not found, set a new value of the key to 1 
        else:
            char_dict[char] += 1 # If found, update the existing value by 1 of the key
    return char_dict
# Returns a sorted list of dictionaries
def get_chars_sorted_list(chars_dict):
    sorted_dict = []
    for char in chars_dict:
        sorted_dict.append({"char": char, "num": chars_dict[char]})
    sorted_dict.sort(reverse=True, key=sort_on) # sort() sorts the list of dictionaries(descending order) 
    return sorted_dict
# Receives a dictionary input and returns the value of the "num" key
def sort_on(dict):
    return dict["num"]