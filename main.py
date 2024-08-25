def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begining report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = count_words(text) 
    print(f"{num_words} words found in the document\n")
    char_count = get_char_dict(text)
    print_char_dict(char_count)
    print("--- End of report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def get_char_dict(text):
    char_count = {}
    for word in text:
        word = word.lower()
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def print_char_dict(char_dict):
    char_dict_list = char_dict_to_list(char_dict)
    def sort_on(dict):
        return(dict["num"]) 
    char_dict_list.sort(reverse=True, key=sort_on)
    for dict in char_dict_list:
        if dict["letter"].isalpha():
            print(f"The '{dict['letter']}' character was found {dict['num']} times")

def char_dict_to_list(dict):
    dict_list = []
    for key in dict:
        dict_list.append({"letter": key, "num": dict[key]})
    return dict_list

main()