
# is staff ?

from is_tag import is_tag
from source_parse import source_expand

# check a message

def is_staff(client, msg):


    if is_tag(msg, 'oper'):

        return True


    if msg['HOST'].lower() in ['localhost', '127.0.0.1']:

        return True


    else:

        for pattern in client.profile['OPERHOST']:

            if pattern.lower() in msg['SRC'].lower():

                return True


    return False


# check a source

def src_is_staff(client, src):


    nick, addr, user, host = source_expand(src)

    if host.lower() in ['localhost', '127.0.0.1']:

        return True


    else:

        for pattern in client.profile['OPERHOST']:

            if pattern.lower() in src.lower():

                return True


    return False
