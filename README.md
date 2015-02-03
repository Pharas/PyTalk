PyTalk
======

A program for the Raspberry Pi that allows the capture of audio and transfers it as text to an IRC client. We are currently using a Python Library called Speech Recognition 1.1.0 for the code to interpret the speech itself. You can find the Library here: http://github.com/Uberi/speech_recognition and here: http://pypi.python.org/pypi/SpeechRecognition/

The source code also includes a windows version of the program.

We will also be hosting the finished package over on [PyPI](https://pypi.python.org/pypi).

Installing and Running
--------
Download Python 2.7 from http://www.python.org/download/releases/2.7/ if you do not already have it.

The libraries used are:

  - Speech Recognition 1.1.0. This library is included in the source. You can visit the library at       http://pypi.python.org/pypi/SpeechRecognition/

  - PyAudio. This library is a dependency for the Speech Recognition library. You can visit the library at http://people.csail.mit.edu/hubert/pyaudio/.
You can build this library on the pi by running: `sudo apt-get install python-pyaudio`

A FLAC encoder is needed. Most distributions have a FLAC package. If not, download the flac package from your package manager. I use [Synaptic](http://www.neil-black.co.uk/install-a-graphical-package-manager-on-the-raspberry-pi#.VCIyqPldWSp] as my package manager) as my package manager. You can also try [rpmfind.net](http://rpmfind.net/linux/rpm2html/search.php?query=flac) or [Debian FLAC](http://packages.debian.org/cgi-bin/search_packages.pl?keywords=flac&searchon=names&subword=1&version=all&release=all). You could also just run `sudo apt-get install flac`

Run main.py from the source code to use the program.

Using the program
--------
Once you run main.py, you will be asked for information on setting up the IRC bot for outputting audio to an IRC channel. The default channel is ##pytalk-test on freenode.

After you input the IRC bot info, the program will start listening for audio. If the audio is unreadable, try speaking more clearly in the mic.

If you say "goodbye", the program will terminate and create a log file that includes what was said and at what time.
