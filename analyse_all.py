from os import listdir
from os.path import isfile, join

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-g", "--galleries_dir", dest="galleries_dir",
                  help="Directory with all galleries",
                  default="/run/media/mike/HUNIEWICZ/photography")
parser.add_option("-o", "--output", dest="output",
                  help="write CSV output to FILE")
parser.add_option("-q", "--quiet",
                  action="store_true", dest="quiet", default=False,
                  help="don't print stats")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="print warning messages")

(options, args) = parser.parse_args()

galleries_dir = options.galleries_dir
gallery_dirs = [f for f in listdir(galleries_dir)
    if not isfile(join(galleries_dir, f))]

import analyser

stats = []

for gallery_dir in gallery_dirs:
    gallery_index = join(galleries_dir, gallery_dir, 'gallery.yaml')
    if isfile(gallery_index):
        text_stats = analyser.analyse_gallery_yaml(gallery_index)
        stats.append([gallery_dir, text_stats])
        if options.quiet is False:
            print "%s: %s" % (gallery_dir, text_stats)
    else:
        if options.verbose is True and options.quiet is False:
            print('WARNING: File %s does not exist.'% gallery_index)

if options.output != None:
    import csv
    with open(options.output, 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["name", "word_count", "unique_word_count", "sentence_count",
            "word_per_sentence_count", "flesch_reading_ease", "polarity",
            "subjectivity"])
        for stat in stats:
            writer.writerow([stat[0], stat[1].word_count,
                stat[1].unique_word_count, stat[1].sentence_count,
                stat[1].word_per_sentence_count, stat[1].flesch_reading_ease,
                stat[1].polarity, stat[1].subjectivity])
