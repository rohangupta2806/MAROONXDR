# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Inline comments for some methods in primitives_maroonx.py
- Inline comments for all methods in primitives_maroonx_echelle.py
- addVAR() method
- Dynamic wavelength calibration
- Method descriptions for methods in primitives_maroonx_echelle.py
- Integration with DRAGONS caldb
## [0.1.2] - 2023-06-14

### Added

- Added "complete" tests, simple scripts that create darks and flats that can be used by an end user to test their 
installation.
- Added some documentation about how an end user can use these tests to test their installation
- Finished adding comments to the primitives_maroonx_echelle.py file
### Changed
- Changed the import paths of all tests to be absolute so that they are more robust

### Known Issues
- Currently the tests in find_stripes and 2 tests in checkND fail.  Looking into this.

## [0.1.1] - 2023-06-13

### Added

- Added .pylintrc file to project with edits to disable some pylint warnings and use camelCase for method names
- Added method descriptions for primitives in primitives_maroonx_echelle.py to README.md
- Added some explanation on how to ensure correct operation of provided unit tests to README.md

### Changed

- Formatted log messages in primitives_maroonx.py to use fstring in accordance with PyLint
- Changed import statements in test files and for primitives_maroonx.py to be more robust (previous implementation was not working)

## [0.1.0] - 2023-06-12

### Added

- Initial Changelog
- Initial README.md
- simple_test.py added for basic test to see that package runs

### Changed

- Filter size changed from 20x20 to 21x21 to ensure compatibility with photutils
- Corrected stackDarks method to be compatible with DRAGONS 3.1

### Removed

- Removed readme.txt (contents moved to README.md)
- Removed previously added installation instructions (contents moved to README.md)