
# save /NAMES list to /members

from chan_privs import chan_privs
from source_parse import source_expand


def namesave(client, channel, unsorted):

    csvlines = []

    for status in unsorted:

        for member in sorted(unsorted[status], key=str.lower):

            if not member: continue

            if member[0] in chan_privs():
                prefix, src = member[0], member[1:]
            else:
                prefix, src = '', member

            nick, addr, user, host = source_expand(src)

            csvlines.append( ','.join([prefix+nick, user, host]) )

    csvlines.insert(0, 'nick,user,host')


    # construct filename
    def safename(s):
        s, safe = s.lower().replace('#', ''), ''
        for c in s: safe += c if (c in 'abcdefghijklmnopqrstuvwxyz012345679-') else '_'
        return safe if safe else '_'
    namesfile  = client.ircpath + '/members/names-'
    namesfile += safename(client.isupport['NETWORK']) + '.'
    namesfile += safename(channel) + '.csv'

    # write csv file
    with open(namesfile, 'w') as f: f.write('\n'.join(csvlines) + '\n')
