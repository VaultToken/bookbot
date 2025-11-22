import string

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_count(string):
    wc = len(string.split())
    return wc

def char_counts(s: str) -> dict:
    counts = {}
    string = s.lower()
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_on(d):
    return d["num"]

def sort_chars_desc(dict):
    sorted_list = []
    for ch in dict:
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": dict[ch]})
        else:
            continue
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list