

# handle oper GLOBAL

from input import input_HELP
from time_calc import now


def handle(client, kb_args):

    if not kb_args[0]:
        input_HELP.handle(client, ['GLOBAL'])
        return None

    if not client.opered:
        print(now(), 'Error:', 'you are not an IRC operator!')
        return

    text = '\x20'.join(kb_args)
    if not text: return

    if client.ircd_family in ['solanum', 'ergo']:
        target = "$$*"
    elif client.ircd_family in ['unreal']:
        target = '$*'
    else: # default
        target = "$$*"

    if client.ircd_family in ['ergo']:
        text = 'GLOBAL: ' + text

    client.sock_send(['NOTICE', target, ':' + text])
