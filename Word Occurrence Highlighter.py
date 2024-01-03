# highlighting and counting occurrence of a specific word in a given text.

"""
Highlight and count the occurrence of a specific word in a given text.

Parameters:
- text (str): The input text
- target_word (str): The word to search for highlight

Returns:
- str: The modified text with occurrence of the target word highlighted
- int: The total number of occurrence of the targeted word
"""

def highlight_word_occurrence(text, targeted_word):
    # Convert target word to lower case for case insensitivity comparison
    targeted_word_lower = targeted_word.lower()

    # Split the text into the words
    words = text.split()

    # Highlight occurrence and count
    occurrence_count = 0
    for i in range(len(words)):
        word_lower = words[i].lower()
        if word_lower == targeted_word_lower:
            # Highlight the word using ANSI escape code or red text
            words[i] = f"\033[1;31m{words[i]}\033[0m"
            occurrence_count += 1

    # Join the words back into modified text
    modified_text = ''. join(words)
    return modified_text, occurrence_count

def main():
    # Take the user input for the text and target word
    user_text = input("Enter your text: ")
    user_target_word = input("Enter the word to highlight: ")

    # Highlight word occurrence
    modified_text, occurrence_count = highlight_word_occurrence(user_text, user_target_word)

    # Display the result
    print("\nModified Text:")
    print(modified_text)
    print(f"\nTotal occurrences of '{user_target_word}': {occurrence_count}")


if __name__ == "__main__":
    main()




