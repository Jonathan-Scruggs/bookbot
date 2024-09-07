def char_sorter(e):
    return e["count"]

def char_dict_to_sorted_list(dict):
    list = []
    for key,value in dict.items():
        list.append({"char":key,"count":value})
    list.sort(reverse=True, key=char_sorter)
    return list
def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] +=1
            else:
                char_counts[char] = 1
    return char_counts

def main():

    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(word_count)
        character_counts = count_characters(file_contents)
        print(character_counts)
        character_counts = char_dict_to_sorted_list(character_counts)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for entry in character_counts:
            character = entry["char"]
            char_count = entry["count"]
            print(f"The {character} character was found {char_count} times")
        print("--- End report ---")
if __name__ == "__main__":
    main()

