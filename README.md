# IPod Shuffle 4g Scripts

##shuffle.py

Python script for building the Track and Playlist database for the newer gen IPod Shuffle.
Forked from the [shuffle-db-ng project](https://code.google.com/p/shuffle-db-ng/)

Just put your audio files into the mass storage of your IPod and shuffle.py will do the rest
```bash
$ python shuffle.py -h
usage: shuffle.py [-h] [--disable-voiceover] [--rename-unicode]
                  [--track-gain TRACK_GAIN]
                  path

positional arguments:
  path

optional arguments:
  -h, --help            show this help message and exit
  --disable-voiceover   Disable Voiceover Feature
  --rename-unicode      Rename Files Causing Unicode Errors, will do minimal
                        required renaming
  --track-gain TRACK_GAIN
                        Store this volume gain (0-99) for all tracks; 0
                        (default) means no gain and is usually fine; e.g. 60
                        is very loud even on minimal player volume
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

From the **Extra** repository: `pacman -S python2 mutagen` and from the AUR: `svox-pico-bin` ([link](https://aur.archlinux.org/packages/svox-pico-bin/))

##### Gentoo Linux

```bash
PYTHON_TARGETS="python2_7" emerge -av media-libs/mutagen
layman --add=ikelos
layman --overlays="https://raw.githubusercontent.com/ahippo/rhvoice-gentoo-overlay/master/repositories.xml" --fetch --add=ahippo-rhvoice-overlay
ACCEPT_KEYWORDS="~amd64" emerge -av app-accessibility/svox app-accessibility/rhvoice
```
References to the overlays above: [ikelos](http://git.overlays.gentoo.org/gitweb/?p=dev/ikelos.git;a=summary), [ahippo-rhvoice-overlay](https://github.com/ahippo/rhvoice-gentoo-overlay)

##TODO
* Last.fm Scrobbler
* Qt frontend

##EXTRA READING
* [shuffle3db specification](docs/iTunesSD3gen.md)
* [Using shuffle.py and Rhythmbox for easy syncing of playlists and songs](http://nims11.wordpress.com/2013/10/12/ipod-shuffle-4g-under-linux/)

The original shuffle3db website went offline. This repository contains a copy of the information inside the `docs` folder.
Original data can be found via [wayback machine](https://web.archive.org/web/20131016014401/http://shuffle3db.wikispaces.com/iTunesSD3gen).
