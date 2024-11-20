

# handle user M(SG)

from input import input_HELP
from message_echo import message_echo


def handle(client, kb_args):

    if len(kb_args) < 2:
        input_HELP.handle(client, ['MSG']); return

    target   = kb_args[0]
    if not target: return None

    sentence = '\x20'.join( kb_args[1:] )

    emitter  = [ 'PRIVMSG' , target , ':' + sentence ]

    client.sock_send( emitter )

    message_echo(client, emitter)

