#!/usr/bin/env python
# encoding: utf-8

# Copyright (c) 2013  Herve BREDIN (http://herve.niderb.fr/)
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import argparse
import os
import sys
import bbc

parser = argparse.ArgumentParser(
    description='Get EastEnders cast and synposis from BBC Programmes API.')

parser.add_argument('json', type=str,
                    help='path to directory where JSON metadata files are '
                         'stored (e.g. eastenders/metadata/')

parser.add_argument('--cast', type=str,
                    help='path to existing directory where cast lists should '
                         'be downloaded (e.g. /tmp/cast/)')

parser.add_argument('--synopsis', type=str,
                    help='path to existing directory where synopses should '
                         'be downloaded (e.g. /tmp/synposis/)')

args = parser.parse_args()

# get unique resource identifier (one per episode)
uris = [name[:-5] for name in os.listdir(args.json) if name[-5:] == '.json']

# initialize BBC Programme API
api = bbc.BBCProgrammes(args.json)

# process one episode at at time
for u, uri in enumerate(uris):

    # feedback to the user
    sys.stdout.write('%d/%d | Episode %s\n' %
                     (u+1, len(uris), uri))

    # get metadata for current episode
    data = api(uri)

    # save cast information to file
    if hasattr(args, 'cast'):
        with open('%s/%s.txt' % (args.cast, uri), 'w') as f:
            for actor in data['cast']:
                f.write('%s|%s|%s\n' % actor)

    # save synopsis to file
    if hasattr(args, 'synopsis'):
        with open('%s/%s.txt' % (args.synopsis, uri), 'w') as f:
            f.write('%s' % data['synopsis'])
