from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--input", dest="input",
                  help="CSV file with galleries",
                  default="/tmp/galleries.csv")
(options, args) = parser.parse_args()

import pandas as pd
df = pd.read_csv(options.input)

print("Most words:")
print(df.sort_values(['word_count'], ascending=[0]).head(10)[['name', 'word_count']])

print("Fewest words:")
print(df.sort_values(['word_count'], ascending=[1]).head(10)[['name', 'word_count']])

print("Most unique words:")
print(df.sort_values(['unique_word_count'], ascending=[0]).head(10)[['name', 'unique_word_count']])

print("Fewest unique words:")
print(df.sort_values(['unique_word_count'], ascending=[1]).head(10)[['name', 'unique_word_count']])

print

print("Average unique words: %f" % df["unique_word_count"].mean())

print

print("Longest sentences:")
print(df.sort_values(['word_per_sentence_count'], ascending=[0]).head(10)[['name', 'word_per_sentence_count']])

print("Shortest sentences:")
print(df.sort_values(['word_per_sentence_count'], ascending=[1]).head(10)[['name', 'word_per_sentence_count']])

print

print("Most positive galleries:")
print(df.sort_values(['polarity'], ascending=[0]).head(10)[['name', 'polarity']])

print("Least positive galleries:")
print(df.sort_values(['polarity'], ascending=[1]).head(10)[['name', 'polarity']])

print

print("Most subjective galleries:")
print(df.sort_values(['subjectivity'], ascending=[0]).head(10)[['name', 'subjectivity']])

print("Least subjective galleries:")
print(df.sort_values(['subjectivity'], ascending=[1]).head(10)[['name', 'subjectivity']])

print

print("Most easy to read galleries:")
print(df.sort_values(['flesch_reading_ease'], ascending=[0]).head(10)[['name', 'flesch_reading_ease']])

print("Least easy to read galleries:")
print(df.sort_values(['flesch_reading_ease'], ascending=[1]).head(10)[['name', 'flesch_reading_ease']])
