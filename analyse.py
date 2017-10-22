test_data = ''

import re
def prepare(original_line):
    line = re.sub('<.*?>', '', original_line)
    line = re.sub('\s+', ' ', line)
    line = re.sub('\[[0-9]+\]', ' ', line)
    line = re.sub('&[a-z]+;', '', line)
    line = line.strip()
    return line

import yaml
with open('gallery.yaml', 'r') as f:
    doc = yaml.load(f)
    description = prepare(doc["description"])
    test_data = test_data + description
    for p in doc["photos"]:
        test_data = test_data + ' ' + prepare(p['description'])

from textblob import TextBlob
zen = TextBlob(test_data)
print('Word count: ' + str(len(zen.words)))
print('Sentence count: ' + str(len(zen.sentences)))
print('Sentiment: ' + str(zen.sentiment))

from textstat.textstat import textstat
print('Words per sentence: ' +
    str(textstat.lexicon_count(test_data, False) /
        textstat.sentence_count(test_data)))

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


test_data = test_data.lower()

ps = PorterStemmer()
words = word_tokenize(test_data)

test_data = ''

for w in words:
    test_data = test_data + ' ' + ps.stem(w)

words = word_tokenize(test_data)

nonPunct = re.compile('.*[A-Za-z0-9].*')  # must contain a letter or digit
filtered = [w for w in words if nonPunct.match(w)]
s2 = set(['that', '\'s', 'wa', 'thi'])
from nltk.corpus import stopwords
s = set(stopwords.words('english'))
filtered = [w for w in filtered if w not in s2 and w not in s]


from collections import Counter
counts = Counter(filtered)
print('Unique words: ' + str(len(counts)))

print(counts.most_common(5))
# print(stopwords.words('english'))
