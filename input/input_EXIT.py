

# handle user EXIT

from sys import exit


def handle(client, kb_args):

    client.reconnect = 0

    client.connection_reset()

    exit('EXIT: QUIT .')

