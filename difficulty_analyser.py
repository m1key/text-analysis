# For a given text, unique words are extracted.
# Common words are removed.
# Then, difficulty is established for each word.

from os import listdir
from os.path import isfile, join
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-g", "--galleries_dir", dest="galleries_dir",
                  help="Directory with all galleries",
                  default="/run/media/mike/HUNIEWICZ/photography")

(options, args) = parser.parse_args()

galleries_dir = options.galleries_dir
gallery_dirs = [f for f in listdir(galleries_dir)
    if not isfile(join(galleries_dir, f))]

import analyser

entire_text = ''

for gallery_dir in gallery_dirs:
    gallery_index = join(galleries_dir, gallery_dir, 'gallery.yaml')
    if isfile(gallery_index):
        gallery_text = analyser.extract_plain_text_from_gallery_yaml(gallery_index)
        entire_text = entire_text + ' ' + gallery_text

from nltk.tokenize import word_tokenize
import re

words = word_tokenize(entire_text.lower())

nonPunct = re.compile('.*[A-Za-z].*')
filtered = [w for w in words if nonPunct.match(w)]

# Remove stopwords:
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
extra_stopwords = set(['that', '\'s', 'wa', 'thi', 'like', 'n\'t', 'would',
    'ha', 'us', 'get', '\'m'])
filtered = [w for w in filtered if w not in stopwords
    and w not in extra_stopwords]

from collections import Counter
counts = Counter(filtered)

print("Unique word count is %d" % len(counts))

import difficulty
d = difficulty.Difficulty();
import unicodecsv as csv
with open('/tmp/word_difficulty.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["word", "difficulty", "author"])
    for word in counts:
        word_difficulty = d.get_word_difficulty(word)
        print("[%s]: %d" % (word, word_difficulty))
        writer.writerow([word, word_difficulty, "Michal"])

# Rather than show word count, show percentage.
func = lambda x: 100*x.count()/df.shape[0]

import pandas as pd
df = pd.read_csv('/tmp/word_difficulty.csv')
ax = df.pivot_table(values='word', index='difficulty',
    aggfunc=func).plot(kind='line', legend = False)
ax.set_ylabel("Percentage of Total Words")
ax.set_xlabel("Word Difficulty")

import matplotlib.pyplot as plt
axes = plt.gca()
axes.set_ylim([0, 30])
plt.savefig('/tmp/word_difficulty.png')
