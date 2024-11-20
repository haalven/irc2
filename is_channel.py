
# is a valid channel name ?

from time_calc import now


def is_channel(client, channel):

    # check argument type

    if type(channel) != str: return False

    if not channel: return False


    # comma is not allowed

    if ',' in channel:

        print(now(), chr(9888) + chr(65039), ' comma is not allowed in channel names:', channel)

        return False


    # channel type

    chantypes = client.isupport['CHANTYPES'] if 'CHANTYPES' in client.isupport else ''

    if not chantypes: chantypes = '#&' # default

    if not (channel[0] in chantypes):

        print(now(), chr(9888) + chr(65039), ' not a valid channel type:', channel)

        return False

    # OK.

    return True

