

# display formatted messages

from copy import deepcopy
from time_calc import pre
from xterm_control import color, endcol, light, normal


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )

    verb     = deepcopy( msg['VERB'] )

    src      = deepcopy( msg['SRC']  )

    text     = deepcopy( '\x20'.join(msg['PAR']) )


    # source

    if not src.strip():
        src = client.myserv if client.myserv else '-server-'


    # formatting

    verb     = color(72) + '['+verb+']' + endcol()

    src      = light() + '(from: '+src+')' + normal()


    # construct and print

    line   = [ date , verb , text , src ]

    print( '\x20'.join(line) )

