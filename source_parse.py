
# parse nick!user@host


def source_parse(msg):

    msg['NICK'], _, msg['ADDR'] = msg['SRC'].partition('!')

    msg['ID'],   _, msg['HOST'] = msg['ADDR'].partition('@')

    return msg


def source_expand(src):

    nick, _, addr = src.partition('!')

    user, _, host = addr.partition('@')

    return(nick, addr, user, host)
