
# check blacklist

from copy import deepcopy
from time_calc import dt_now
from datetime import timedelta
from text_lines import text_lines


def update_blacklist(client):

    blacklist = set()

    for line in text_lines(client.ircpath + '/blist.txt'):

        pattern, _, comment = line.partition('\x20')

        if pattern: blacklist.add(pattern.lower())

    client.blackset  = deepcopy(blacklist)

    client.blackdate = dt_now()



def blacklist(client, msg):

    msg['BLACK'] = []

    if not msg['SRC']: return


    # source and account

    src = msg['SRC'].lower()

    acc = msg['TAGS']['account'].lower() if 'account' in msg['TAGS'] else ''


    # blacklist outdated?

    if (dt_now() - client.blackdate) > timedelta(seconds=1):

        update_blacklist(client)


    # check

    for pattern in client.blackset:

        if (pattern in src) or (pattern in acc):

            msg['BLACK'].append(pattern)



def isblack(client, src):

    if not src: return

    src = src.lower()


    # blacklist outdated?

    if (dt_now() - client.blackdate) > timedelta(seconds=1):

        update_blacklist(client)


    for pattern in client.blackset:

        if pattern in src:

            return True

    return False
