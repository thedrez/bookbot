def get_num_words(text):
    number_of_words = text.split()
    print(len(number_of_words), "words found in the document")

def get_char_counts(text):
    char_counts = {}
    lowercase_text = text.lower()
    for character in range(0,len(lowercase_text)):
        my_char = lowercase_text[character]
        #print(my_char)
        if my_char in list(char_counts):
            #print("found: ",my_char," with value:",char_counts[my_char])
            char_counts.update({my_char: char_counts[my_char] + 1})
        else:
            #print("must add: ",my_char)
            char_counts.update({my_char: 1})

    print(char_counts)

