

# handle user CM (casemapped)

from input import input_HELP
from casemapping import casemapped
from time_calc import now
from xterm_control import color, endcol


def handle(client, kb_args):

    string = '\x20'.join(kb_args).strip()

    if not string:
        input_HELP.handle(client, ['CM']); return

    cmap = client.casemap if client.casemap else '[none]'

    cm = casemapped(client, string)

    print( now() , 'casemapped:' , color(6) + cm + endcol() , '('+ cmap +')' )

