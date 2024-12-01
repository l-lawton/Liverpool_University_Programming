def count_words_in_text(dictionary_file, text_file):
    # Open and read the dictionary file to get the list of words to search for
    with open(dictionary_file, 'r') as dict_file:
        dictionary_words = [line.strip().lower() for line in dict_file]

    # Open and read the text file
    with open(text_file, 'r') as txt_file:
        text = txt_file.read().lower()

    # Initialize a dictionary to store the count of each word
    word_counts = {word: 0 for word in dictionary_words}

    # Split the text into words using spaces (and other whitespace)
    text_words = text.split()

    # Count occurrences of each dictionary word in the text
    for word in text_words:
        word = word.strip('.,!?"')  # Remove common punctuation characters
        if word in word_counts:
            word_counts[word] += 1

    # Print the counts for each word in the dictionary
    for word in dictionary_words:
        print(f"{word}: {word_counts[word]}")

# Example usage
count_words_in_text('dictionary.txt', 'text.txt')
