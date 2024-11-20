
# IRC message parser


def msg_parser(line):

    # tags parser (IRCv3)

    TAGS = {}

    if line[0] == '@':

        tagmsg, _, line = line.partition('\x20')

        for tag in tagmsg[1:].split(';'):

            key, _, value = tag.partition('=')

            TAGS[key] = value


    # preserve trailing message

    line, hastrail, trailing = line.partition('\x20:')


    # parameter list

    PAR  = list(filter(bool, line.split('\x20')))


    # source and verb

    SRC  = PAR.pop(0)[1:] if PAR[0][0] == ':' else ''

    VERB = PAR.pop(0).upper()


    # append trailing message and return

    if hastrail: PAR.append(trailing)

    return {'SRC':SRC, 'VERB':VERB, 'PAR':PAR, 'TAGS':TAGS}

