
# in ISUPPORT ?


def real_key(key):

    return key.split('/')[-1] if '/' in key else key


def is_isupport(client, key):

    for active in client.isupport:

        if real_key(key.lower()) == real_key(active.lower()):

            return True

    return False
