def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        num_words = get_num_words(book)
        words = book.split()
        
        chars_dict = get_chars_dict(book)
        print(chars_dict)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document")
        print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

        print("--- End report ---")


def get_num_words(book):
    words = book.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

main()

