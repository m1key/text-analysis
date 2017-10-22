from os import listdir
from os.path import isfile, join

galleries_dir = '/run/media/mike/HUNIEWICZ/photography'
gallery_dirs = [f for f in listdir(galleries_dir)
    if not isfile(join(galleries_dir, f))]

import analyser

for gallery_dir in gallery_dirs:
    gallery_index = join(galleries_dir, gallery_dir, 'gallery.yaml')
    if isfile(gallery_index):
        text_stats = analyser.analyse_gallery_yaml(gallery_index)
        print(text_stats)
    else:
        print('File %s does not exist.'% gallery_index)
    print
