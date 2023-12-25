def get_book_text():
    with open("./books/frankenstein.txt") as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_alphabetic_characters(text):
    chars_count = {}
    for char in text:
        if char.isalpha():
            character = char.lower()
            if character in chars_count:
                chars_count[character] += 1
            else:
                chars_count[character] = 1
    return chars_count

def print_report(word_count, chars_count):
    separator = "-" * 28
    print(separator)
    print("\tEND OF TEXT")
    print(separator)
    print(f"Words: {word_count} words") 
    print("Charactes in text: ")
    for char in chars_count: 
        print(f"\t{char} appeared {chars_count[char]} times")

def main():
    book_text = get_book_text()
    word_count = count_words(book_text)
    # Count characters and saves it as a dictionary
    chars_count = count_alphabetic_characters(book_text)
    
    print(book_text)
    print_report(word_count, chars_count)
    
main()
