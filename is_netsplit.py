
# is netsplit ?

from xterm_control import color, light, reset


def is_netsplit(quitmsg):


    if '\x20' in quitmsg:

        svr = quitmsg.split('\x20')

        if len(svr) == 2:

            if ('.' in svr[0]) and ('.' in svr[1]):

                split = [svr[0], reset() + color(92) + chr(215) + light(), svr[1] + reset()]

                return '\x20'.join(split)

    return quitmsg
