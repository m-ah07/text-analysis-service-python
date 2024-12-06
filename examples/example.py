from src.text_analyzer import TextAnalyzer

if __name__ == "__main__":
    text = "This is a sample text. It demonstrates the text analysis service. The text analyzer works well!"
    analyzer = TextAnalyzer(text)

    print("Word count:", analyzer.count_words())
    print("Character count (with spaces):", analyzer.count_characters())
    print("Character count (without spaces):", analyzer.count_characters(include_spaces=False))
    print("Sentence count:", analyzer.count_sentences())
    print("Frequent words:", analyzer.find_frequent_words())
