def word_count(print_book):
    to_split = print_book
    split = print_book.split()
    return len(split)

def char_count(file_contents):
    counter_dict = {}
    for char in file_contents:
        converted_char = char.lower()
        if converted_char in counter_dict:
            counter_dict[converted_char] += 1
        else:
            counter_dict[converted_char] = 1    
            # Remove this print statement
    return counter_dict

def sort_on(dict):
    return list(dict.values())[0]

def sorted_dict(character_counter):
    list_of_dicts = []
    for key in character_counter:
        new_dict = {key: character_counter[key]}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts