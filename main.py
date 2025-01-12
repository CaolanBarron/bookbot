"""This script reads a book from a specified file and returns data on it"""

def main():
    """
    Main function to examine a book text file.

    
    """
    book_path = "books/frankenstein.txt"
    book_text  = get_book_text(book_path)
    word_count = count_words(book_text)
    print(word_count)
    quantified_characters = quanity_characters(book_text)

    filtered_character_quantities = []

    for key, num in quantified_characters.items():
        if  not key.isalpha():
            continue

        filtered_character_quantities.append({"char": key, "amount": num })

    filtered_character_quantities.sort(reverse=True, key=sort_on)

    for item in filtered_character_quantities:
        print(f"The '{item['char']}' character was found {item['amount']} times")


def sort_on(dic):
    """Sorts by the characters amount"""
    return dic['amount']


def count_words(book_text):
    """
    Count the number of words in a given text.

    Args:
        book_text (str): The text of the book as a string.

    Returns:
        int: The total number of words in the text.
    """
    words = book_text.split()
    return len(words)


def quanity_characters(text):
    """
    Count the amount of times each character appears in the text

    Args:
        book_text (str): The text of the book as a string

    Returns:
        dict: The amount of times each character appears
    """
    result = {}
    for letter in text:
        formatted_letter = letter.lower()
        if formatted_letter not in result:
            result[formatted_letter] = 0
        result[formatted_letter] += 1
    return result


def get_book_text(path):
    """
    Read the content of a text file at the specified path.

    Args:
        path (str): The path to the text file.

    Returns:
        str: The content of the file as a string.
    """
    with open(path, encoding='utf-8') as f:
        return f.read()



main()
