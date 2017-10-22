from os import listdir
from os.path import isfile, join

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-g", "--galleries_dir", dest="galleries_dir",
                  help="Directory with all galleries",
                  default="/run/media/mike/HUNIEWICZ/photography")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="print warning messages")

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
    else:
        if options.verbose is True and options.quiet is False:
            print('WARNING: File %s does not exist.'% gallery_index)

global_stats = analyser.analyse_plain_text(entire_text)
print(global_stats)
