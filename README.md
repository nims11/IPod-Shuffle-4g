# IPod Shuffle 4g Scripts

##shuffle.py

Python script for building the Track and Playlist database for the newer gen IPod Shuffle.
Forked from the [shuffle-db-ng project](https://code.google.com/p/shuffle-db-ng/)

Just put your audio files into the mass storage of your IPod and shuffle.py will do the rest
```bash
$ python shuffle.py -h
usage: shuffle.py [-h] [--disable-voiceover] [--rename-unicode] path

positional arguments:
  path

optional arguments:
  -h, --help           show this help message and exit
  --disable-voiceover  Disable Voiceover Feature
  --rename-unicode     Rename Files Causing Unicode Errors, will do minimal
                       required renaming
```

#### Additions to the original
* Option to disable voiceover
* Initialize the IPod Directory tree
* Using the --rename-unicode flag, filenames with strange characters and different language are renamed which avoids the script to crash with a Unicode Error

#### Dependencies

This script requires:

* [Python 2.7](http://www.python.org/download/releases/2.7/)
* [Mutagen](https://code.google.com/p/mutagen/)
* [PicoSpeaker](http://picospeaker.tk/readme.php) -- for non-Russian files
* [RHVoice (master branch, 3e31edced402a08771d2c48c73213982cbe9333e)](https://github.com/Olga-Yakovleva/RHVoice) -- for Russian files only
* [SoX](http://sox.sourceforge.net) -- for Russian files only

##### Ubuntu

`apt-get install python-mutagen libttspico*`

##### Arch Linux

From the **Extra** repository: `pacman -S python2 mutagen` and from the AUR: `svox-pico-git` ([link](https://aur.archlinux.org/packages/svox-pico-git/))

##### Gentoo Linux

`PYTHON_TARGETS="python2_7" emerge -av media-libs/mutagen`
`layman --add=ikelos` ([ikelos](http://git.overlays.gentoo.org/gitweb/?p=dev/ikelos.git;a=summary))
`ACCEPT_KEYWORDS="~amd64" emerge -av app-accessibility/svox`

##TODO
* Last.fm Scrobbler
* Qt frontend

##EXTRA READING
* [Using shuffle.py and Rhythmbox for easy syncing of playlists and songs](http://nims11.wordpress.com/2013/10/12/ipod-shuffle-4g-under-linux/)

