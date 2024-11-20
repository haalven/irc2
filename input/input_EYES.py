

# handle user EYES

from input import input_HELP
from message_echo import message_echo


def handle(client, kb_args):

    if not kb_args[0]:
        input_HELP.handle(client, ['EYES']); return

    target = kb_args[0]

    emitter = [ 'PRIVMSG' , target , ':' + chr(128064) ]

    client.sock_send( emitter )

    message_echo(client, emitter)

