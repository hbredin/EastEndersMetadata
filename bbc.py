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

import json
import requests

BBC_URL = 'http://www.bbc.co.uk/programmes'


class BBCProgrammes(object):

    def __init__(self, pathToJSON):
        super(BBCProgrammes, self).__init__()
        self.pathToJSON = pathToJSON

    def __call__(self, uri):

        # load eastenders/metadata/XXXXX.json file
        path = '%s/%s.json' % (self.pathToJSON, uri)
        with open(path, 'r') as f:
            data = json.load(f)

        # get episode and version pids from it
        try:
            episode = data['episode']['pid']
        except:
            print 'No episode pid for %s' % uri
            episode = None

        try:
            version = data['version']['pid']
        except:
            print 'No version pid for %s' % uri
            version = None

        # get episode metadata from BBC Programmes
        episode_data = None
        if episode:
            try:
                url = '%s/%s.json' % (BBC_URL, episode)
                r = requests.get(url)
                episode_data = r.json()
            except:
                print 'Error requesting %s' % url
                # episode_data = None

        # get version metadata from BBC Programmes
        version_data = None
        if version:
            try:
                url = '%s/%s.json' % (BBC_URL, version)
                r = requests.get(url)
                version_data = r.json()
            except:
                print 'Error requesting %s' % url
                # version_data = None

        result = {}
        if episode_data:
            result['synopsis'] = episode_data['programme']['long_synopsis']
        else:
            result['synopsis'] = ''

        if version_data:
            actors = []
            for contributor in version_data['version']['contributors']:
                if contributor['role'] == 'Actor':
                    character_name = contributor['character_name']
                    last_name = contributor['family_name']
                    first_name = contributor['given_name']
                    actors.append((first_name, last_name, character_name))
            result['cast'] = actors
        else:
            result['cast'] = []

        return result
