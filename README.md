
Python scripts for EastEnders metadata extraction
(for TRECVid 2013 Instance Search task)

For each episode in TRECVid 2013 INS, this script will download the cast and a
longer synopsis than the one provided in the original metadata file, using
the [BBC Programmes API](http://www.bbc.co.uk/programmes).

Enjoy!

Prerequisites
-------------

- access to TRECVid INS 2013 corpus
- [requests](http://docs.python-requests.org/en/latest/) Python library

Usage
-----

    $ python run.py --help
    usage: run.py [-h] [--cast CAST] [--synopsis SYNOPSIS] json

    Get EastEnders cast and synposis from BBC Programmes API.

    positional arguments:
      json                 path to directory where JSON metadata files are stored
                           (e.g. eastenders/metadata/

    optional arguments:
      -h, --help           show this help message and exit
      --cast CAST          path to existing directory where cast lists should be
                           downloaded (e.g. /tmp/cast/)
      --synopsis SYNOPSIS  path to existing directory where synopses should be
                           downloaded (e.g. /tmp/synposis/)

License
-------

    Copyright (c) 2013  Herve BREDIN (http://herve.niderb.fr/)
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
        * Redistributions of source code must retain the above copyright
          notice, this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
          notice, this list of conditions and the following disclaimer in the
          documentation and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.
