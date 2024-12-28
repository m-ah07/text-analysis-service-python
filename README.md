# Text Analysis Service (Python)

A Python-based service for performing advanced text analysis, including:
- Counting words, characters, and sentences.
- Identifying the most frequent words.
- Supporting customizable options like excluding stopwords.

---

## 🚀 Features
- **Word Count**: Count the total words in the text.
- **Character Count**: Count characters with or without spaces.
- **Sentence Count**: Count the number of sentences in the text.
- **Frequent Words**: Identify the top frequent words in the text.

## 🔧 Installation
Clone the repository:
```bash
git clone https://github.com/marwan-ahmed-23/text-analysis-service-python.git
```


## 📖 Usage
Here's how to use the service:

```bash
from src.text_analyzer import TextAnalyzer

text = "This is an example text for analysis."
analyzer = TextAnalyzer(text)

print("Word count:", analyzer.count_words())
print("Character count:", analyzer.count_characters())
print("Sentence count:", analyzer.count_sentences())
print("Frequent words:", analyzer.find_frequent_words())
```

## 📂 Directory Structure
```plaintext
text-analysis-service-python/
├── examples/
│   └── example.py
├── src/
│   ├── __init__.py
│   └── text_analyzer.py
├── LICENSE
├── .gitignore
└── README.md
```

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to enhance functionality or add features.

## 🌟 Show Your Support
If you found this project helpful, please consider giving it a ⭐ on GitHub. Your support means the world to us!
