import sys
from stats import get_book_word_num, count_chars, pretty_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents   
    

def main():
    try:
        path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(path)  
    num_words = get_book_word_num(file_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    char_dict = count_chars(file_contents)
    pretty_report = pretty_dict(char_dict)
    
    for item in pretty_report:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()
