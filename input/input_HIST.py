

# handle user HIST

from time_calc import now
from is_cap import is_cap
from is_isupport import is_isupport
from input import input_HELP
from am_i_in import am_i_in


def handle(client, kb_args):

    chan = kb_args[0]


    # check CAPs

    hist_type = ''

    if is_cap(client, 'playback'): hist_type = 'znc'

    elif is_cap(client, 'chathistory'): hist_type = 'ircv3'

    elif is_isupport(client, 'CHATHISTORY'): hist_type = 'ircv3'


    if not hist_type:

        print(now(), 'history/playback is not supported by this server .')

        return None


    # check argument

    if not chan: input_HELP.handle(client, ['HIST']); return None

    if not am_i_in(client, chan): return


    # history command

    match hist_type:

        case 'znc':   command = ['ZNC', '*playback', 'PLAY', chan, '0']

        case 'ircv3': command = ['HISTORY', chan, '100']

    client.sock_send(command)

