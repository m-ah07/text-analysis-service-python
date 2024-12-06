class TextAnalyzer:
    """
    TextAnalyzer: A class to perform various text analysis operations.

    Methods:
        - count_words: Returns the number of words in a text.
        - count_characters: Returns the number of characters (with and without spaces).
        - count_sentences: Returns the number of sentences in a text.
        - find_frequent_words: Finds the most frequent words in a text.
    """

    def __init__(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split())

    def count_characters(self, include_spaces=True):
        return len(self.text) if include_spaces else len(self.text.replace(" ", ""))

    def count_sentences(self):
        return self.text.count('.') + self.text.count('?') + self.text.count('!')

    def find_frequent_words(self, exclude_stopwords=True):
        from collections import Counter
        import string

        stop_words = {'and', 'or', 'but', 'the', 'a', 'an', 'in', 'on', 'at', 'to'}
        words = [word.strip(string.punctuation).lower() for word in self.text.split()]
        if exclude_stopwords:
            words = [word for word in words if word not in stop_words]
        return Counter(words).most_common(5)
