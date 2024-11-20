

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    if client.member_save: return None


    # format elements

    date   = pre( msg['DATE'] )

    par    = deepcopy( msg['PAR'] )


    # parse

    channel, username, host, server, nick, flags, trailing = \
        par[1], par[2], par[3], par[4], par[5], par[6], par[7]

    hopcount, _, realname = trailing.partition('\x20')


    # formatting

    #spaces = 4 - len(flags)
    #if spaces > 0: flags += spaces * '\x20'
    flags = flags.replace( '*' , color(88)+'*'+reset() )   # oper

    nick  = color(32) + nick

    addr  = color(33) + username + reset()
    addr += light() + '@' + reset()
    addr += color(33) + host + reset()

    server = light() + '-> ' + server + reset()


    # construct and print

    line = [date, channel, flags, nick, addr, server, realname]

    print( '\x20'.join(line) )

