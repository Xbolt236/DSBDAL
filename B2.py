def separate_words(paragraph):
    # Split the paragraph into words
    words = paragraph.split()
    
    # Dictionary to store word frequencies
    word_counts = {}
    
    # Count the frequency of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Separate repeated and non-repeated words
    repeated_words = []
    non_repeated_words = []
    
    for word, count in word_counts.items():
        if count > 1:
            repeated_words.append(word)
        else:
            non_repeated_words.append(word)
    
    return repeated_words, non_repeated_words

# Example usage
paragraph = "This is a sample paragraph with some repeated words. This paragraph contains words like sample, paragraph, repeated, and words."
repeated, non_repeated = separate_words(paragraph)
print("Repeated words:", repeated)
print("Non-repeated words:", non_repeated)

