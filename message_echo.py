
# "echoing" your own text messages
# if there is no active "echo-message" cap
# the emitter argument is a 3-list [VERB, TARGET, TEXT]
# TEXT must start with ':'

from is_cap import is_cap
from is_mynick import is_mynick
from msg_process import msg_process


def message_echo(client, emitter):

    # check CAPs
    if is_cap(client, 'echo-message'): return None

    # split emitter
    VERB, TARGET, TEXT = emitter

    # loop message?
    if is_mynick(client, TARGET): return None

    # compile command
    cmd = f'{VERB} {TARGET} {TEXT}'

    # add source
    src = client.mynick
    msg = f':{src} {cmd}'

    # encode
    line = msg.encode('utf-8')

    # send to process
    msg_process(client, line)

