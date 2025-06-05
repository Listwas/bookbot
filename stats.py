
def get_book_word_num(file):
    count_words = len(file.split())
    return count_words

def count_chars(file):
    word_list = file.split()

    characters = []   
    for word in word_list:
        for char in word:
            characters.append(char.lower())
    
    dict = {}
    for char in characters: 
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_dict(dict):
    return dict["num"]

def pretty_dict(char_dict):
    result = []

    for char in char_dict:
        num = char_dict[char]
        entry = {"char": char, "num": num}
        result.append(entry)

    result.sort(key=sort_dict, reverse=True)

    
    return result 


