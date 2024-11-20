

# handle user WHOX

from input import input_HELP
from is_isupport import is_isupport
from time_calc import now


def handle(client, kb_args):

    if not is_isupport(client, 'WHOX'):
        print(now(), 'WHOX is not supported by this server .')
        return None

    if (not kb_args[0]) or (len(kb_args) > 1):
        input_HELP.handle(client, ['WHOX']); return

    mask = kb_args[0]

    client.sock_send([ 'WHO' , mask , '%tcuihsnfdlaor,999' ])

