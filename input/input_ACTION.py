

# handle user ACTION

from input import input_HELP
from message_echo import message_echo


def handle(client, kb_args):

    if len(kb_args) < 2:
        input_HELP.handle(client, ['ACTION']); return

    target   = kb_args[0]

    if not target: return None

    sentence = '\x20'.join( kb_args[1:] )

    action   = '\x01' + 'ACTION' + '\x20' + sentence + '\x01' 

    emitter  = [ 'PRIVMSG' , target , ':' + action ]

    client.sock_send( emitter )

    message_echo(client, emitter)

