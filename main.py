import sys
def main():
    book_path = "books/frankenstein.txt"
    text = read_book_contents(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_word_report(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def read_book_contents(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c.isalnum():
            if c in chars:
                chars[c]+=1
            else:
                chars[c] = 0
    return chars

def print_word_report(dict_word):
    sorted_dict = dict(sorted(dict_word.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dict.items():
        print(f"The '{key}' character was found {value} times")


if __name__ == '__main__':
    sys.exit(main())