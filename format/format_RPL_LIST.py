

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import bold,light,reset


def format(client,msg):

    if client.top_list  or client.save_list: return None


    # elements

    date   = pre( msg['DATE'] )

    channel= deepcopy( msg['PAR'][1] )

    members= deepcopy( msg['PAR'][2] )

    topic  = deepcopy( msg['PAR'][3] ) if len(msg['PAR'])>3 else ''


    # formatting

    channel = bold() + channel + reset()

    topic = light() + topic + reset()


    # construct

    line = [ date , channel , str(members) , topic ]

    print( '\x20'.join(line) )

