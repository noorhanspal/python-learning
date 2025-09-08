# Program to count frequency of words in a sentence

def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()   # case-insensitive
        freq[word] = freq.get(word, 0) + 1
    return freq


# Example usage
if __name__ == "__main__":
    sentence = "Python is easy and Python is powerful"
    print("Sentence:", sentence)
    print("Word Frequency:", word_frequency(sentence))
