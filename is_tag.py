
# returns a valid key in msg['TAGS'] or False
# e.g. is_tag(msg, '+typing') -> '+draft/typing'

from copy import deepcopy


def is_tag(msg, tagname):

    for tag in msg['TAGS']:

        realtag = deepcopy(tag)

        usertag = tag.startswith('+')

        if usertag: realtag = realtag[1:]

        realtag = realtag.split('/')[-1]

        if usertag: realtag = '+' + realtag

        if tagname.lower() == realtag.lower():

            return tag

    return False
