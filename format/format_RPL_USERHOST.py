

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date   = pre( msg['DATE'] )

    verb   = '[UH]'

    userhosts = deepcopy( msg['PAR'][1] ) if len(msg['PAR'])>1 else ''

    uh_list   = userhosts.split('\x20') if '\x20' in userhosts else [userhosts]


    for uh in uh_list:

        if not uh: continue

        nick, _, addr = uh.partition('=')

        if nick.endswith('*'):
            isop = True
            nick = nick[:-1]
        else: isop = False

        isaway = addr[0]
        addr   = addr[1:]

        username, _, host = addr.partition('@')


        # formatting

        nick  = color(32) + nick

        addr  = color(33) + username + reset()
        addr += light() + '@' + reset()
        addr += color(33) + host + reset()


        # construct and print

        line = [ date , verb , nick , addr ]

        if isop: line.append('is oper')

        if isaway == '-': line.append('(away)')

        print( '\x20'.join(line) )

