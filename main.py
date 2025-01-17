def main():
    path_to_file = "books/frankenstein.txt"
    book_contents = read_book(path_to_file)
    wordcount = get_num_words(book_contents)
    lettercount = get_letter_count(book_contents)
    print_report(path_to_file,wordcount,lettercount)

def read_book(book):
    with open(book) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    count_dict = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter != " ":
            if lower_letter not in count_dict:
                count_dict[lower_letter] = 1
            else:
                count_dict[lower_letter] += 1
    return count_dict

def print_report(book,count,dictionary):
    sorted_dict = sort_dict(dictionary)
    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in the document")
    print("")
    print_list_dict(sorted_dict)
    print("--- End report ---")


def sort_dict(dict):
    mylist = []
    for key, value in dict.items():        
        if key.isalpha():
            mylist.append({"char": key, "count": value})
    mylist.sort(reverse=True, key=sort_on)
    return mylist

def sort_on(dict):
    return dict["count"]

def print_list_dict(dict):
    for item in dict:
        letter = (item["char"])
        count = (item["count"])
        print(f"The '{letter}' character was found {count} times")

main()