# Python interface for sending flags, timestamps, messages to EGI's NetStation EEG Acquisition software

## Version Info
Current Release: 0.20.0
Supported systems: any OS, NetStation 4.3+, NetStation 5.2+ (needs confimation on NetStation support)

## Background
I've been maintaining/updating this code for the past ~6 years.
It's been updated most recently to work in Python 3.7,
but should work in any version of Python 3.x (needs confirmation).

## Updates TODO:
-Add NTP timing infrastructure
-Clean up and re-document
-Handle errors
-Generate log-files for emergency cases (e.g. experiment crashes but timestamps still saved)
-Better handle multiple versions of NetStation (4.x-5.x)

## Contribute
If you use this library please consider contributing to it's longevity by:
-Add documentation example from your experiment
-Create Markdown documentation
-Testing updates
-Provide timing files from your calibration tests along with system information (computer specs, software specs, etc.)

## Contact/Support
If you have questions/suggestions, please contact me at: joshua.e.zosky@gmail.com


This is a clone of pynetstation from https://code.google.com/p/pynetstation/.
As far as I can tell, the repository is no longer maintained.  The original
reposity went with the name pynetstation because it is based off of
the C library libnetstation.  I renamed it to python-egi because the
python module is called egi.
