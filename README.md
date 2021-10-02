# IPod Shuffle 4g Script

## ipod-shuffle-4g.py

Python script for building the Track and Playlist database for the newer gen IPod Shuffle.
Forked from the [shuffle-db-ng project](https://code.google.com/p/shuffle-db-ng/)
and improved my nims11 and NicoHood.

Just put your audio files into the mass storage of your IPod and shuffle.py will do the rest.
```
$ ./ipod-shuffle-4g.py --help
usage: ipod-shuffle-4g.py [-h] [-t] [-p] [-u] [-g TRACK_GAIN]
                          [-d [AUTO_DIR_PLAYLISTS]] [-i [ID3_TEMPLATE]] [-v]
                          path

Python script for building the Track and Playlist database for the newer gen
IPod Shuffle. Version 1.5

positional arguments:
  path                  Path to the IPod's root directory

optional arguments:
  -h, --help            show this help message and exit
  -t, --track-voiceover
                        Enable track voiceover feature
  -p, --playlist-voiceover
                        Enable playlist voiceover feature
  -u, --rename-unicode  Rename files causing unicode errors, will do minimal
                        required renaming
  -g TRACK_GAIN, --track-gain TRACK_GAIN
                        Specify volume gain (0-99) for all tracks; 0 (default)
                        means no gain and is usually fine; e.g. 60 is very
                        loud even on minimal player volume
  -d [AUTO_DIR_PLAYLISTS], --auto-dir-playlists [AUTO_DIR_PLAYLISTS]
                        Generate automatic playlists for each folder
                        recursively inside "IPod_Control/Music/". You can
                        optionally limit the depth: 0=root, 1=artist, 2=album,
                        n=subfoldername, default=-1 (No Limit).
  -i [ID3_TEMPLATE], --auto-id3-playlists [ID3_TEMPLATE]
                        Generate automatic playlists based on the id3 tags of
                        any music added to the iPod. You can optionally
                        specify a template string based on which id3 tags are
                        used to generate playlists. For eg. '{artist} -
                        {album}' will use the pair of artist and album to
                        group tracks under one playlist. Similarly '{genre}'
                        will group tracks based on their genre tag. Default
                        template used is '{artist}'
  -v, --verbose         Show verbose output of database generation.
```

#### Dependencies

This script requires:
* [Python 3](https://www.python.org/download/releases/3.0/)

Optional album/artist and auto-id3-playlists support:
* [Mutagen](https://code.google.com/p/mutagen/)

Optional Voiceover support
* [eSpeak](http://espeak.sourceforge.net/)
* [PicoSpeaker](http://picospeaker.tk/readme.php)
* [RHVoice (master branch, 3e31edced402a08771d2c48c73213982cbe9333e)](https://github.com/Olga-Yakovleva/RHVoice) -- (Russian files only)
* [SoX](http://sox.sourceforge.net) -- (Russian files)
* say (macOS)

##### Ubuntu

`apt-get install python3 python-mutagen libttspico*`

##### Arch Linux

From the **Extra** repository: `pacman -S python` and optional `pacman -S python-mutagen espeak` or from the AUR: `svox-pico-bin` ([link](https://aur.archlinux.org/packages/svox-pico-bin/))

You can also [install the script from AUR](https://aur.archlinux.org/packages/ipod-shuffle-4g/).

##### Gentoo Linux

```bash
PYTHON_TARGETS="python3" emerge -av media-libs/mutagen
layman --add=ikelos
layman --overlays="https://raw.githubusercontent.com/ahippo/rhvoice-gentoo-overlay/master/repositories.xml" --fetch --add=ahippo-rhvoice-overlay
ACCEPT_KEYWORDS="~amd64" emerge -av app-accessibility/svox app-accessibility/rhvoice
```
References to the overlays above: [ikelos](http://git.overlays.gentoo.org/gitweb/?p=dev/ikelos.git;a=summary), [ahippo-rhvoice-overlay](https://github.com/ahippo/rhvoice-gentoo-overlay)

## Tips and Tricks

#### Disable trash for IPod
To avoid that linux moves deleted files into trash you can create an empty file `.Trash-1000`.
This forces linux to delete the files permanently instead of moving them to the trash.
Of course you can also use `shift + delete` to permanently delete files without this trick.
The file can be found in the [extras](extras) folder.

#### Compress/Convert your music files
([#11](https://github.com/nims11/IPod-Shuffle-4g/issues/11)) Shuffle is short on storage, and you might want to squeeze in more of your collection by sacrificing some bitrate off your files. In rarer cases, you might also possess music in formats not supported by your ipod. Although `ffmpeg` can handle almost all your needs, if you are looking for a friendly alternative, try [Soundconverter](http://soundconverter.org/).

#### Use Rhythmbox to manage your music and playlists
As described [in the blog post](https://nims11.wordpress.com/2013/10/12/ipod-shuffle-4g-under-linux/)
you can use Rythmbox to sync your personal music library to your IPod
but still make use of the additional features this script provides (such as voiceover).

Simply place a file called `.is_audio_player` into the root directory of your IPod and add the following content:
```
name=&quot;Name's IPOD&quot;
audio_folders=iPod_Control/Music/
```
The file can be found in the [extras](extras) folder.

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

#### Format/Restore/Recover IPod
([#41](https://github.com/nims11/IPod-Shuffle-4g/issues/41)) If you formatted your IPod wrong and lost all data you can still recover it.
It is important to **not use MBR/GPT**. You need to directly create a **Fat16 Filesystem**:

```bash
sudo mkfs.vfat -I -F 16 -n IPOD /dev/sdX
```

Run this script to generate the new database. All missing sound files should be regenrated by the IPod on next use.
Your IPod should work and play music again now.

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
