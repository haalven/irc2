

# handle user (J)OIN

from input import input_HELP
from is_channel import is_channel


def handle(client, kb_args):

    channel = kb_args[0]

    if not channel: input_HELP.handle(client, ['J']); return None

    chans = channel.split(',')

    for c in chans:

        if not is_channel(client, c): return None


    client.sock_send([ 'JOIN' , '\x20'.join( kb_args ) ])
