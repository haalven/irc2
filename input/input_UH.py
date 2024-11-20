

# handle user UH

from input import input_HELP


def handle(client, kb_args):

    if not kb_args[0]:
        input_HELP.handle(client, ['UH'])
        return None

    nicks = '\x20'.join(kb_args)

    if nicks:

        client.sock_send([ 'USERHOST' , nicks ])
