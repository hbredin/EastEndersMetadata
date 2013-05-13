import json
import requests

JSON_DIR = '/vol/corpora4/tvseries/EastEnders/eastenders/metadata/'
BBC_URL = 'http://www.bbc.co.uk/programmes'
SYNOPSIS_DIR = '/tmp/synopsis/'
ACTOR_DIR = '/tmp/actors/'


class BBCProgrammes(object):

    BBC_URL = 'http://www.bbc.co.uk/programmes'

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

with open('uris.lst', 'r') as f:
    uris = [u.strip() for u in f.readlines()]

metadata = BBCProgrammes(JSON_DIR)

for u, uri in enumerate(uris):

    print "%d/%d -- %s" % (u+1, len(uris), uri)
    data = metadata(uri)

    with open('%s/%s.txt' % (SYNOPSIS_DIR, uri), 'w') as f:
        f.write('%s' % data['synopsis'])

    with open('%s/%s.txt' % (ACTOR_DIR, uri), 'w') as f:
        for actor in data['cast']:
            f.write('%s|%s|%s\n' % actor)
