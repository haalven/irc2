

# handle user QUIT

from sys import exit
from rand_stuff import randquit


def handle(client, kb_args):

    # construct quitmsg

    quitmsg = '' # this will be sent

    if kb_args == ['']: # no argument
        quitmsg = randquit(client)

    elif kb_args == [':']: # empty msg
        pass

    else: # there is a msg
        quitmsg = '\x20'.join(kb_args)
        if quitmsg.startswith(':'):
            quitmsg = quitmsg[1:] # remove it


    # send quit and close the client

    client.reconnect = 0

    client.sock_send(f'QUIT :{quitmsg}')

    client.connection_reset()

    exit('EXIT: QUIT .')

