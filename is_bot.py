
# is bot ?

from is_tag import is_tag


def is_bot(client, msg):

    # letters only
    nick, ident, host, acc = '', '', '', ''
    letters = 'abcdefghijklmnopqrstuvwxyz'


    # in message-tags?
    if is_tag(msg, 'bot'): return True

    # in nickname?
    for c in msg['NICK'].lower():
        if c in letters: nick += c
    if nick.endswith('bot'): return True

    # in ident?
    if msg['ID'].lower() in ['~limnoria', '~sopel']: return True
    for c in msg['ID'].lower():
        if c in letters: ident += c
    if ident.endswith('bot'): return True

    # in host?
    host = msg['HOST'].lower()
    if '/bot/' in host: return True
    if host.endswith('bot'): return True
    if host.startswith('bot.'): return True
    for p in ['eggdrop','ircdriven','doo.l4c.slpjik.ip']:
        if p in host: return True

    # in account?
    if 'account' in msg['TAGS']:
        for c in msg['TAGS']['account'].lower():
            if c in letters: acc += c
        if acc.endswith('bot'): return True


    # nothing found
    return False
