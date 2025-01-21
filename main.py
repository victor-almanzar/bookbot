from string import ascii_lowercase
from string import whitespace
def read_book():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    return len(book.split())

def count_characters(book):
    alphabet = [i for i in ascii_lowercase] + [i for i in whitespace]
    count = {}
    for alphabet_letter in alphabet:
        count[alphabet_letter] = 0
    for book_letter in book:
        for alphabet_letter in alphabet:
            if book_letter.lower() == alphabet_letter:
                count[alphabet_letter] += 1
    return count

def sort_on(dict):
        return dict['count']

def make_char_list(count):
    char_list = []
    for char in count:
        if char in ascii_lowercase:
            char_list.append({'char': char, 'count': count[char]})
    return char_list
# 
def main():
    book = read_book()
    total_words = count_words(book)
    total_chars = count_characters(book)
    total_chars_list = make_char_list(total_chars)
    total_chars_list.sort(reverse=True, key=sort_on)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{total_words} words found in the document')
    for char in total_chars_list:
        print(f"The '{char['char']}' character was found {char['count']} times")
    print('--- End report ---')
main()