

# display formatted messages

from copy import deepcopy
from umode_list import umode_list
from is_mynick import is_mynick
from time_calc import pre
from xterm_control import color,light,reset


def format(client,msg):

    # format elements

    date    = pre( msg['DATE'] )

    nick    = deepcopy( msg['NICK'] )

    umode   = deepcopy(msg['PAR'][1])

    mode    = '\x20'.join( deepcopy(msg['PAR'][1:]) )


    # umodes_list

    umodes_list = umode_list(client, umode) if client.ircd_family else []


    # formatting

    if not nick: nick = deepcopy( client.myserv )

    if is_mynick(client, msg['NICK']):

        nick, verb = 'You', 'set user mode:'

    else: verb = 'sets user mode:'

    mode = color(166) + mode + light()

    um_list = str(umodes_list) + reset()


    # construct and print

    line = [ date , nick , verb , mode , um_list ]

    print( '\x20'.join(line) )

