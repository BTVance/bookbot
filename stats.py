def word_in_book(text):
    split = text.split()
    num_words = (len(split))
    return num_words

def char_in_book(text):
   lower_text = text.lower()
   char_count = {}

   for char in lower_text:
       if char in char_count:
           char_count[char] += 1
       else:
           char_count[char] = 1
        
   return char_count

def sort_chars(char_count):
    chars_list = []

    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list

def print_report(word_count, sort_character):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sort_character:
        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")