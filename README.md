# Text Analysis

Sandbox Python project for some text stats. Will be applied to my gallery yaml
files.

## Setup

Using Python 2. Anaconda installed.

`pip install textstat`

`pip install nltk`

`>>> import nltk`

`>>> nltk.download('punkt')`

`>>> nltk.download('english')`

`pip install textblob`

`pip install pyaml`

## Simple run

This will analyse a local file.

`python analyse.py`

## Analyse All Galleries

This will analyse all galleries, assuming they are under the default directory.

`python analyse_all.py`

Make it verbose to see problems:

`python analyse_all.py -v`

You can store the output as CSV:

`python analyse_all.py -o /tmp/galleries.csv`

Use `--help` for all options.

`python analyse_all.py --help`
