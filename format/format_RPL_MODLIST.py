

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import bold,reset


def format(client,msg):

    # elements  (InspIRCd /MODULES)

    date   = pre( msg['DATE'] )

    module = deepcopy( msg['PAR'][1] )

    infos  = []

    for p in msg['PAR'][2:]:

        if p != '*': infos.append(p)

    info = '\x20'.join(infos)


    # formatting

    module = bold() + module + reset()


    # construct

    line = [ date , '[MODULE]' , module , info ]

    print( '\x20'.join(line) )

