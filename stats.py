def get_num_of_words(text):
   num_of_words = text.split()
   return len(num_of_words)

def get_num_of_chars(text):
    num_chars = text.lower()
    chars = {}
    for num_char in num_chars:
        if num_char in chars:
            chars[num_char] += 1
        else:
            chars[num_char] = 1
    return chars
    
def sort_on(dict):
    return dict["count"]

def get_sorted_list(num_chars):
    char_list = []
    for num_char in num_chars:
        # if num_char.isalpha():
        char_dict = {"char": num_char, "count": num_chars[num_char]}
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list