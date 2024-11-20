

# display formatted messages

from copy import deepcopy
from time_calc import pre


def format(client, msg):

    # format elements

    date = pre(msg['DATE'])

    std_type  = deepcopy(msg['VERB'])

    std_cmd   = deepcopy(msg['PAR'][0])

    try: std_code  = '\x20'.join(deepcopy(msg['PAR'][2:-1]))
    except Exception: std_code = ''

    std_descr = deepcopy(msg['PAR'][-1])


    # formatting

    symbol = chr(9888)+chr(65039)+'\x20'


    # construct and print

    if std_code:

        line   = [date, symbol, std_type, std_cmd + ':', std_code, '('+std_descr+')']

    else:

        line   = [date, symbol, std_type, std_cmd, '('+std_descr+')']

    print( '\x20'.join(line) )

