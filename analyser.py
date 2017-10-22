from __future__ import division

class TextStats():
        word_count = 0
        unique_word_count = 0
        sentence_count = 0
        word_per_sentence_count = 0
        polarity = 0
        subjectivity = 0
        counts = None

        def __str__(self):
            return(("[word count: %d, unique word count: %d, " +
                "sentence count: %d, word per sentence count: %f, " +
                "polarity: %f, subjectivity: %f, most common words: %s]") %
                    (self.word_count, self.unique_word_count,
                        self.sentence_count,
                        self.word_per_sentence_count, self.polarity,
                        self.subjectivity, self.counts.most_common(5)))

# Cleanse the data.
import re
def prepare(original_line):
    line = re.sub('<.*?>', '', original_line)
    line = re.sub('\s+', ' ', line)
    line = re.sub('\[[0-9]+\]', ' ', line)
    line = re.sub('&[a-z]+;', '', line)
    line = line.strip()
    return line

def analyse_plain_text(test_data) :
    text_stats = TextStats()

    # Do some simple analysis.
    from textblob import TextBlob
    zen = TextBlob(test_data)
    text_stats.word_count = len(zen.words)
    text_stats.sentence_count = len(zen.sentences)
    text_stats.polarity = zen.sentiment.polarity
    text_stats.subjectivity = zen.sentiment.subjectivity

    from textstat.textstat import textstat
    text_stats.word_per_sentence_count = (textstat.lexicon_count(test_data, False) /
        textstat.sentence_count(test_data))

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
    extra_stopwords = set(['that', '\'s', 'wa', 'thi', 'like', 'n\'t', 'would',
        'ha', 'us', 'get'])
    filtered = [w for w in filtered if w not in stopwords and w not in extra_stopwords]

    # How many unique words?
    from collections import Counter
    counts = Counter(filtered)
    text_stats.unique_word_count = len(counts)

    # Words sorted by most common.
    text_stats.counts = counts

    return text_stats


def analyse_gallery_yaml(file_name) :
    plain_text = extract_plain_text_from_gallery_yaml(file_name)

    return analyse_plain_text(plain_text)


def extract_plain_text_from_gallery_yaml(file_name) :
    # Grab only text from the yaml file.
    test_data = ''
    import yaml
    with open(file_name, 'r') as f:
        doc = yaml.load(f)
        description = prepare(doc["description"])
        test_data = test_data + description
        for p in doc["photos"]:
            test_data = test_data + ' ' + prepare(p['description'])

    return test_data
