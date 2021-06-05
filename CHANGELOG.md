# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
This changlog uses the [ISO 8601 date format](https://www.iso.org/iso-8601-date-and-time-format.html) of (YYYY-MM-DD).

## [Unreleased]

## [1.5.1] - 2021-06-05

### Changed

* Moved Changelog from Readme to Changelog.md file

### Fixed

* Fix TypeError when reading playlist files [#50](https://github.com/nims11/IPod-Shuffle-4g/pull/50)

## [1.5.0] - 2020-06-10

### Changed

* Port Script to Python3
* Mutagen support is now optional

## [1.4.0] - 2016-08-28

### Added

* Added optional `--verbose` output
* Added files to `extras` folder
* Added shortcut parameters (`-p`, `-t`, `-d`, etc.)

### Changed

* Renamed `--voiceover` to `--track-voiceover`
* Renamed script from `shuffle.py` to `ipod-shuffle-4g.py`
* Ignore hidden filenames
* Do not force playlist voiceover with auto playlists

### Fixed

* Catch "no space left" error [#30](https://github.com/nims11/IPod-Shuffle-4g/issues/30)
* Fix UnicodeEncodeError for non-ascii playlist names [#35](https://github.com/nims11/IPod-Shuffle-4g/issues/35)

## [1.3.0] - 2016-06-08

### Added

* Directory based auto playlist building (`--auto-dir-playlists`) [#13](https://github.com/nims11/IPod-Shuffle-4g/issues/13)
* ID3 tags based auto playlist building (`--auto-id3-playlists`)
* Added short program description
* Differentiate track and playlist voiceover [#26](https://github.com/nims11/IPod-Shuffle-4g/issues/26)

### Changed

* Voiceover disabled by default [#26](https://github.com/nims11/IPod-Shuffle-4g/issues/26) (Playlist voiceover enabled with auto playlist generation)


### Fixed

* Fix hyphen in filename [#4](https://github.com/nims11/IPod-Shuffle-4g/issues/4)
* Fixed mutagen bug [#5](https://github.com/nims11/IPod-Shuffle-4g/issues/5)

## [1.2.0] - 2016-02-04

### Added

* Added Path help entry
* Added MIT License
* Added this changelog

### Changed

* Skip existing voiceover files with the same name (e.g. "Track 1.mp3")
* Made help message lower case
* Improved Readme
* Improved docs

### Fixed

* Additional fixes from NicoHood
* Fixed "All Songs" and "Playlist N" sounds when voiceover is disabled [#17](https://github.com/nims11/IPod-Shuffle-4g/issues/17)
* Better handle broken playlist paths [#16](https://github.com/nims11/IPod-Shuffle-4g/issues/16)
* Only use voiceover if dependencies are installed

## [1.1.0] - 2016-01-23

### Added

* Fixes from nims11 fork
* Option to disable voiceover
* Initialize the IPod Directory tree
* Using the `--rename-unicode` flag filenames with strange characters and different language are renamed which avoids the script to crash with a Unicode Error
* Other small fixes

## [1.0.0] - 2012-10-17

### Added

* Original release by ikelos

[Unreleased]: https://github.com/nims11/IPod-Shuffle-4g/compare/1.5.1...HEAD
[1.5.1]: https://github.com/nims11/IPod-Shuffle-4g/compare/v1.5...1.5.1
[1.5.0]: https://github.com/nims11/IPod-Shuffle-4g/compare/v1.4...v1.5
[1.4.0]: https://github.com/nims11/IPod-Shuffle-4g/compare/v1.3...v1.4
[1.3.0]: https://github.com/nims11/IPod-Shuffle-4g/compare/v1.2...v1.3
[1.2.0]: https://github.com/nims11/IPod-Shuffle-4g/compare/v1.1...v1.2
[1.1.0]: https://github.com/nims11/IPod-Shuffle-4g/compare/646b7def4c498c59b063e535a5b64695d8d87e6b...v1.1
[1.0.0]: https://github.com/nims11/IPod-Shuffle-4g/commit/646b7def4c498c59b063e535a5b64695d8d87e6b
