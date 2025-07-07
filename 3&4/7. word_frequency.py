'''a program that defines a function `word_frequency` that takes a sentence as input and
calculates the frequency of each word in the sentence and returns the results as a dictionary.'''

# calculates the frequency of each word in a given sentence.
def word_frequency(sentence):
    words_frequency = {}
    words = sentence.split()

    for word in words:
        if word in words_frequency:
            words_frequency[word] += 1
        else:
            words_frequency[word] = 1

    return words_frequency

# Main execution block to test the function
if __name__ == "__main__":
    # Test Case 1
    test_sentence1 = "hi hello ciao hi ciao namaste"
    print(f"\nProcessing sentence: '{test_sentence1}'")
    frequency_dict1 = word_frequency(test_sentence1)
    print(f"Word Frequencies:\n{frequency_dict1}")

    # Test Case 2
    test_sentence2 = ""
    print(f"\nProcessing sentence: '{test_sentence2}'")
    frequency_dict2 = word_frequency(test_sentence2)
    print(f"Word Frequencies:\n{frequency_dict2}")

    # Test Case 3: User Input
    print("\n--- Test with User Input ---")
    test_sentence3 = input("Enter a sentence: ")
    frequency_dict3 = word_frequency(test_sentence3)
    print(f"Word Frequencies:\n{frequency_dict3}")
