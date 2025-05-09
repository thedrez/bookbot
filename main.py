from stats import get_num_words,get_char_counts


def get_book_text(path_to_book):

    with open(path_to_book, 'r') as book:
        contents_of_book = book.read()

    return contents_of_book


def main():
    text_of_book = get_book_text("books/frankenstein.txt")
    get_num_words(text_of_book)
    testone = "testone"
    #print(len(testone))
    #for character in range(0,len(testone)):
    #    print(testone[character])
    get_char_counts(text_of_book)

if __name__ == "__main__":
    main()
