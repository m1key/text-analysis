# 43 words.
test_data = ''' Perhaps the best way to understand individual countries, and in
Eastern Europe even more so than elsewhere, is to understand their history. In
Poland, we like to boast that Poland was off the maps for 123 years, and yet it
managed to come back to life and gain independence, after all. It turns out that
Bulgaria survived half a millennium under foreign occupation, and yet it stood
the test of time, and preserved its identity. '''

# https://pypi.python.org/pypi/textstat/
from textstat.textstat import textstat

# The boolean is for punctuation symbols.
print('Lexicon count, no punctuation: ' +
    str(textstat.lexicon_count(test_data, False)))

print('Lexicon count, including punctuation: ' +
    str(textstat.lexicon_count(test_data, True)))

print('Sentence count: ' +
    str(textstat.sentence_count(test_data)))

print('Words per sentence: ' +
    str(textstat.lexicon_count(test_data, False) /
        textstat.sentence_count(test_data)))

# * 90-100 : Very Easy
# * 80-89 : Easy
# * 70-79 : Fairly Easy
# * 60-69 : Standard
# * 50-59 : Fairly Difficult
# * 30-49 : Difficult
# * 0-29 : Very Confusing
print('Flesch reading ease: ' + str(textstat.flesch_reading_ease(test_data)))

# For example a score of 9.3 means that a ninth grader would be able to read the
# document.
print('Flesch kincaid grade: ' + str(textstat.flesch_kincaid_grade(test_data)))

# The index estimates the years of formal education a person needs to understand
# the text on the first reading.
print('Gunning FOG: ' + str(textstat.gunning_fog(test_data)))

# The SMOG grade is a measure of readability that estimates the years of
# education needed to understand a piece of writing.
print('SMOG: ' + str(textstat.smog_index(test_data)))

# ARI(Automated Readability Index) which outputs a number that approximates the
# grade level needed to comprehend the text.
print('ARI: ' + str(textstat.automated_readability_index(test_data)))

# Approximates the U.S. grade level thought necessary to comprehend the text.
print('Coleman Liau: ' + str(textstat.coleman_liau_index(test_data)))

# Specifically designed to calculate the United States grade level of a text
# sample. US Air Force.
print('Linsear Write: ' + str(textstat.linsear_write_formula(test_data)))

# 4.9 or lower easily understood by an average 4th-grade student or lower
# 5.0-5.9 easily understood by an average 5th or 6th-grade student
# 6.0-6.9 easily understood by an average 7th or 8th-grade student
# 7.0-7.9 easily understood by an average 9th or 10th-grade student
# 8.0-8.9 easily understood by an average 11th or 12th-grade student
# 9.0-9.9 easily understood by an average 13th to 15th-grade (college) student
print('Dale-Chall Readability Score: ' +
    str(textstat.dale_chall_readability_score(test_data)))

# Built-in overall.
print('Overall grade required to comprehend at first reading: ' +
    str(textstat. text_standard(test_data)))


from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()
words = word_tokenize(test_data)

# for w in words:
#    print(ps.stem(w))

print(len(words))

import re
from collections import Counter

nonPunct = re.compile('.*[A-Za-z0-9].*')  # must contain a letter or digit
filtered = [w for w in words if nonPunct.match(w)]
counts = Counter(filtered)
print(counts)
print('Unique words: ' + str(len(counts)))
