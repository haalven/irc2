

# display formatted messages

from copy import deepcopy
from time_calc import pre
from is_mynick import is_mynick
from xterm_control import color, bold, light, reset


def format(client,msg):

    # format elements

    date     = pre( msg['DATE'] )

    tags     = deepcopy( msg['TAGS'] )

    src      = deepcopy( msg['SRC'] )

    target   = deepcopy( msg['PAR'][0] )


    # formatting


    # target

    if is_mynick(client, msg['PAR'][0]):

        target = color(126) + '[private]' + reset()  # private msg

    else:

        target = light() + '['+ target +']' + reset()  # other msg


    # source, verb

    src       = bold() + src + reset()

    verb      = color(126) + '[TAGMSG]'


    # user tags only (starting with '+')

    user_tags = {}

    for tag in tags:

        if tag.startswith('+'):

            user_tags[tag] = tags[tag]

    taginfo = light() + str(user_tags) + reset()


    # construct and print

    line   = [ date , target , src , verb , taginfo ]

    print( '\x20'.join(line) )

