
# load connection profile

from os.path import exists
from json import load


def load_profile(ircpath, profile_name):

    # create and check path

    profile_path = ircpath + '/profiles/profile-' + profile_name + '.json'

    if not exists(profile_path):
        exit(f'profile "{profile_name}" is missing')

    # load json
    with open(profile_path) as f:
        profile = load(f)

    return profile

