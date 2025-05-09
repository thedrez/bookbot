from stats import create_report

def get_book_text(path_to_book):
    with open(path_to_book, 'r') as book:
        contents_of_book = book.read()
    return contents_of_book

def main():
    relative_path_to_book = "books/frankenstein.txt"
    create_report(relative_path_to_book,get_book_text(relative_path_to_book))

if __name__ == "__main__":
    main()
