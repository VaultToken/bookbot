from stats import get_book_text
from stats import get_book_word_count
from stats import get_book_character_count
from stats import get_book_character_count_sorted

import sys

def main():
    #print("This is the name of the program:", sys.argv[0])
    #print("Argument List:", str(sys.argv))

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    for fp in sys.argv[1:]:

	    #fp = "books/frankenstein.txt"

        print("============ BOOKBOT ============")
        print("Analyzing book found at " + fp + "...")

        print("----------- Word Count ----------")
        bw_count = get_book_word_count(fp)
        print("Found", bw_count, "total words")

        print("--------- Character Count -------")
        get_book_character_count_sorted(fp)

main()