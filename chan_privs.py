
# channel privileges


def chan_privs():

    return {
        '!': 'oper',
        '~': 'owner',
        '&': 'admin',
        '@': 'op',
        '%': 'halfop',
        '+': 'voice'
    }


def priv_modes(client):

    if not 'PREFIX' in client.isupport: return 'ov'

    priv_modes = ''

    for c in 'Yqaohv':

        if c in client.isupport['PREFIX']:

            priv_modes += c

    return priv_modes
