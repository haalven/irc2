

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color, reset


def format(client, msg):

    # format elements

    date   = pre(msg['DATE'])

    par    = deepcopy(msg['PAR'][1:])


    myinfo = []

    for p in par:
        if p != '*': myinfo.append(p)


    # formatting

    verb = color(58) + '[MYINFO]' + reset()


    # construct and print

    for info in myinfo:

        line = [date, verb, info]

        print('\x20'.join(line))

