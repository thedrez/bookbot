import sys
import os
from stats import create_report

def get_book_text(path_to_book):
    with open(path_to_book, 'r') as book:
        contents_of_book = book.read()
    return contents_of_book

def main():
    print(sys.argv[1:])
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        relative_path_to_book = sys.argv[1]

    if not os.path.exists(relative_path_to_book):
        print(f"File {relative_path_to_book} does not exist!")
        sys.exit(1)

    print(f"Found {relative_path_to_book} in filesystem.")
    create_report(relative_path_to_book,get_book_text(relative_path_to_book))

if __name__ == "__main__":
    main()
