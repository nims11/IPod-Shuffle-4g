# IPod Shuffle 4g Scripts

##shuffle.py

Python script for building the Track and Playlist database for the newer gen IPod Shuffle.
Forked from the [shuffle-db-ng project](https://code.google.com/p/shuffle-db-ng/)

Just put your audio files into the mass storage of your IPod and shuffle.py will do the rest
```bash
$ python shuffle.py -h
usage: shuffle.py [-h] [--disable-voiceover] path

positional arguments:
  path

optional arguments:
  -h, --help           show this help message and exit
  --disable-voiceover
```

### Additions to the original
* Option to disable voiceover
* Initialize the IPod Directory tree
