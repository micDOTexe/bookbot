from stats import word_count, char_count, sorted_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    
    text = get_book_text(path) #REMOVED HARD CODED HERE
    
    print("----------- Word Count ----------")
    word_count_result = word_count(text)
    print(f"Found {word_count_result} total words")
    
    print("--------- Character Count -------")
    char_counts = char_count(text)
    sorted_chars = sorted_dict(char_counts)
    
    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")
    
    print("============= END ===============")

if len(sys.argv) < 2:
    print("python3 main.py <path_to_book>")
    sys.exit(1)

main()