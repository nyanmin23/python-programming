def main():
    get_text()


# Get text input from the user
def get_text():
    while True:
        text = input("Text: ")

        # Check if the input text is empty
        if text is None:
            print("Input text should not be empty.")
        # Check if the input text contains only spaces
        elif text[0] == " " or text[-1] == " ":
            print("Input text should not start or end with a space or spaces.")
        else:
            check_readability(text)
            break


# Check the readability of the text based on the Coleman-Liau index
def check_readability(text):
    sentences = count_sentance(text)
    words = count_word(text)
    letters = count_letters(text)
    
    grade_level(sentences, words, letters)


# Count sentences by looking for '.', '!', or '?' at the end of the text
def count_sentance(text) -> int:
    return sum(1 for char in text if char in '.!?')


# Count words by splitting the text by spaces
def count_word(text) -> int:
    return (len(text.split()))


# Count letters by checking if each character is alphabetic
def count_letters(text) -> int:
    return sum(1 for char in text if char.isalpha())


def grade_level(sentence, word, letter):
    S = float(sentence)
    W = float(word)
    L = float(letter)
    
    # Calculate the average number of letters per 100 words.
    avg_letter = (L / W) * 100
    # Calculate the average number of sentences per 100 words.
    avg_sentence = (S / W) * 100
    # Calculate the readability index using Coleman-Liau index formula
    grade = (0.0588 * avg_letter) - (0.296 * avg_sentence) - 15.8    
    index = int(round(grade))

    # Print the grade level based on the index
    print(f"Grade {index}") if index > 1 and index <= 10 else print("Before Grade 1")

    if index > 10:
        print("Grade 16+")


if __name__ == "__main__":
    main()