def get_book_text(path_to_book):

    with open(path_to_book, 'r') as book:
        contents_of_book = book.read()

    return contents_of_book

def print_word_count(text_of_book):
    words = text_of_book.split()
    print(len(words), "words found in the document")


def main():
    text_of_book = get_book_text("books/frankenstein.txt")
    print_word_count(text_of_book)

if __name__ == "__main__":
    main()
