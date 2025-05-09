def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    number_of_words = text.split()
    return len(number_of_words)

def get_char_counts_dict(text):
    char_counts_dict = {}
    lowercase_text = text.lower()
    for character in range(0,len(lowercase_text)):
        my_char = lowercase_text[character]
        #print(my_char)
        if my_char in list(char_counts_dict):
            #print("found: ",my_char," with value:",char_counts_dict[my_char])
            char_counts_dict.update({my_char: char_counts_dict[my_char] + 1})
        else:
            #print("must add: ",my_char)
            char_counts_dict.update({my_char: 1})

    #print(char_counts_dict)
    return char_counts_dict

def get_sorted_char_count_array(unsorted_char_count_dict):
    sorted_char_count_array = []
    for key,value in unsorted_char_count_dict.items():
        if key.isalpha():
            sorted_char_count_array.append({"char": key, "num": value})
    
    #print(type(sort_on(sorted_char_count_array[0])))

    sorted_char_count_array.sort(reverse=True, key=sort_on)
    #print(sorted_char_count_array)
    return sorted_char_count_array

def create_report(relative_path_to_book,book_text):
    print("============ BOOKBOT ============")
    print("Analyzing book found at",relative_path_to_book,"...")
    print("----------- Word Count ----------")
    print("Found",get_num_words(book_text),"total words")
    print("--------- Character Count -------")
    for item in get_sorted_char_count_array(get_char_counts_dict(book_text)):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

