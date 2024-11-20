

# handle user SHRUG

from input import input_HELP
from message_echo import message_echo


def handle(client, kb_args):

    if not kb_args[0]:
        input_HELP.handle(client, ['SHRUG']); return

    target = kb_args[0]

    emitter = [ 'PRIVMSG' , target , ':' + '¯\\_(ツ)_/¯' ]

    client.sock_send( emitter )

    message_echo(client, emitter)
