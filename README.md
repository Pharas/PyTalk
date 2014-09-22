PyTalk
======

A program for Raspberry Pi that allows the capture of audio and transfers it as text to an IRC client. We are currently using a Python Library called Speech Recognition 1.1.0 for the code to interpret the speech itself. You can find the Library here: http://github.com/Uberi/speech_recognition and here: http://pypi.python.org/pypi/SpeechRecognition/
We will also be hosting the finished package over on Pypi.

Installing and Running
--------
1. Download Python 2.7 from http://www.python.org/download/releases/2.7/ if you do not already have it.

2. The libraries used are:
    - Speech Recognition 1.1.0. This library is included in the source. You can visit the library at       http://pypi.python.org/pypi/SpeechRecognition/
    - PyAudio. This library is also included in the source. You can visit the library at http://people.csail.mit.edu/hubert/pyaudio/. You can build this library on the pi by running::
 sudo apt-get install python-pyaudio

3. A FLAC encoder is needed. Most distributions have a FLAC package, use the package manager to get FLAC. If not, try 
http://rpmfind.net/linux/rpm2html/search.php?query=flac or http://packages.debian.org/cgi-bin/search_packages.pl?keywords=flac&searchon=names&subword=1&version=all&release=all

4. Run main.py from the source code to use the program.

Quickstart
--------
To be filled in
