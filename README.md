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

##Tips and Tricks

#### Disable trash for IPod
To avoid that linux moves deleted files into trash you can create an empty file `.Trash-1000`.
This forces linux to delete the files permanently instead of moving them to the trash.
Of course you can also use `shift + delete` to permanently delete files without this trick.

#### Use Rhythmbox to manage your music and playlists
As described [in the blog post](https://nims11.wordpress.com/2013/10/12/ipod-shuffle-4g-under-linux/)
you can use Rythmbox to sync your personal music library to your IPod
but still make use of the additional features this script provides (such as voiceover).

Simply place a file called `.is_audio_player` into the root directory of your IPod and add the following content:
```
name=&quot;Name's IPOD&quot;
audio_folders=iPod_Control/Music/
```

Now disable the IPod plugin of Rhythmbox and enable the MTP plugin instead.
You can use Rythmbox now to generate playlists and sync them to your IPod.
The script will recognize the .pls playlists and generate a proper iTunesSD file.

##### Known Rhythmbox syncing issues
* Creating playlists with names like `K.I.Z.` will fail, because the FAT Filesystem does not support a dot `.` at the end of a directory/file.
* Sometimes bad ID3 tags can also cause corrupted playlists.

In all cases you can try to update Rythmbox to the latest version, sync again or fix the wrong filenames yourself.

#### Carry the script with your IPod
If you want to use this script on different computers it makes sense
to simply copy the script into the IPod's root directory.

## TODO
* Last.fm Scrobbler
* Qt frontend

## EXTRA READING
* [shuffle3db specification](docs/iTunesSD3gen.md)
* [Using shuffle.py and Rhythmbox for easy syncing of playlists and songs](http://nims11.wordpress.com/2013/10/12/ipod-shuffle-4g-under-linux/)
* [gtkpod](http://www.gtkpod.org/wiki/Home)
* [German Ubuntu IPod tutorial](https://wiki.ubuntuusers.de/iPod/)
* [IPod management apps](https://wiki.archlinux.org/index.php/IPod#iPod_management_apps)

The original shuffle3db website went offline. This repository contains a copy of the information inside the `docs` folder.
Original data can be found via [wayback machine](https://web.archive.org/web/20131016014401/http://shuffle3db.wikispaces.com/iTunesSD3gen).


# Version History

```
1.2 Release (04.02.2016)
* Additional fixes from NicoHood
* Fixed "All Songs" and "Playlist N" sounds when voiceover is disabled #17
* Better handle broken playlist paths #16
* Skip existing voiceover files with the same name (e.g. "Track 1.mp3")
* Only use voiceover if dependencies are installed
* Added Path help entry
* Made help message lower case
* Improved Readme
* Improved docs
* Added MIT License
* Added this changelog

1.1 Release (11.10.2013 - 23.01.2016)
* Fixes from nims11 fork
* Option to disable voiceover
* Initialize the IPod Directory tree
* Using the --rename-unicode flag
  filenames with strange characters and different language are renamed
  which avoids the script to crash with a Unicode Error
* Other small fixes

1.0 Release (15.08.2012 - 17.10.2012)
* Original release by ikelos
```

# License and Copyright

```
Copyright (c) 2012-2016 ikelos, nims11, NicoHood
See the readme for credit to other people.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
