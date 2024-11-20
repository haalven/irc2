
# return the servers channel listmodes


def listmodes(client):

    cmodes = client.isupport['CHANMODES'] if 'CHANMODES' in client.isupport else ''

    if not ',' in cmodes: cmodes = 'beI,'

    lmodes = cmodes.split(',')[0]

    return lmodes
