from stats import word_count
from stats import char_count
from stats import sort_list
import sys

def main():
    try:
        pathfile = sys.argv[1]
        text = get_book_text(pathfile)
        num_words = word_count(text)
        num_chars = char_count(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {pathfile}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in sort_list(num_chars):
            print(f"{i["char"]}: {i["num"]}")
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(pathfile):
    with open(pathfile) as f:
        return f.read()

main()