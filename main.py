from stats import *
import sys

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    #path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    #print(f"Found {num_words} total words")
    
    num_unique_char = char_counts(text)
    num_unique_char_sorted = sort_chars_desc(num_unique_char)
    #print(num_unique_char)
    #print(num_unique_char_sorted)

    print_report(sys.argv[1], num_words, num_unique_char_sorted)

main()