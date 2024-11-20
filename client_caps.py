
# my CAPs

from json import load


def client_caps(client):


    caps_file = client.ircpath + '/caps.json'

    with open(caps_file) as f: caps_dic = load(f)

    return caps_dic['enabled'].keys()


