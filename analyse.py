# Cleanse the data.
import re
def prepare(original_line):
    line = re.sub('<.*?>', '', original_line)
    line = re.sub('\s+', ' ', line)
    line = re.sub('\[[0-9]+\]', ' ', line)
    line = re.sub('&[a-z]+;', '', line)
    line = line.strip()
    return line

def analyse_gallery_yaml(file_name) :
    # Grab only text from the yaml file.
    test_data = ''
    import yaml
    with open(file_name, 'r') as f:
        doc = yaml.load(f)
        description = prepare(doc["description"])
        test_data = test_data + description
        for p in doc["photos"]:
            test_data = test_data + ' ' + prepare(p['description'])

    # Do some simple analysis.
    from textblob import TextBlob
    zen = TextBlob(test_data)
    print('Word count: ' + str(len(zen.words)))
    print('Sentence count: ' + str(len(zen.sentences)))
    print('Sentiment: ' + str(zen.sentiment))

    from textstat.textstat import textstat
    print('Words per sentence: ' +
        str(textstat.lexicon_count(test_data, False) /
            textstat.sentence_count(test_data)))

    # Convert all to lower.
    test_data = test_data.lower()

    # Tokenise.
    from nltk.tokenize import word_tokenize
    words = word_tokenize(test_data)

    # Tokenise stemmed text.
    from nltk.stem import PorterStemmer
    ps = PorterStemmer()
    test_data_stemmed = ''
    for w in words:
        test_data_stemmed = test_data_stemmed + ' ' + ps.stem(w)
    stemmed_words = word_tokenize(test_data_stemmed)

    # Remove non-words.
    nonPunct = re.compile('.*[A-Za-z0-9].*')  # must contain a letter or digit
    filtered = [w for w in stemmed_words if nonPunct.match(w)]

    # Remove stopwords:
    from nltk.corpus import stopwords
    stopwords = set(stopwords.words('english'))
    extra_stopwords = set(['that', '\'s', 'wa', 'thi'])
    filtered = [w for w in filtered if w not in stopwords and w not in extra_stopwords]

    # How many unique words?
    from collections import Counter
    counts = Counter(filtered)
    print('Unique words: ' + str(len(counts)))

    # Most common words.
    print(counts.most_common(5))

analyse_gallery_yaml('gallery.yaml')
