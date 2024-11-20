

# display formatted messages

from copy import deepcopy
from time_calc import pre
from is_mynick import is_mynick
from source_parse import source_expand
from xterm_control import light, color, reset


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )

    src      = deepcopy( msg['SRC']   )

    target   = deepcopy( msg['PAR'][0] )

    ctcp_msg = deepcopy( msg['PAR'][1] ).strip('\x01')

    ctcp_verb, _, ctcp_pars = ctcp_msg.partition('\x20')


    # formatting

    if is_mynick(client, msg['PAR'][0]) or not client.registered:

        target = color(136) + '[private]' + reset()

    else: target = light() + '['+ target +']' + reset()


    nick, addr, _, __ = source_expand(src)

    addr      = light() + addr + reset()

    verb      = color(126) + '[CTCP]'

    ctcp_verb = ctcp_verb + light()

    ctcp_pars = ctcp_pars + reset()


    # construct and print

    line   = [ date , target , nick , addr , verb , ctcp_verb , ctcp_pars ]

    print( '\x20'.join(line) )

