
# display outgoing messages

from time_calc import pre
from xterm_control import color, reset


def display_send(client, msg, stripped):

    # hide PING replies
    if msg['VERB']=='PONG' and client.hide_ping: return None

    # hide `keep-alive` PINGs
    if msg['VERB']=='PING':
        if len( msg['PAR'] ) > 0:
            if msg['PAR'][0] == 'keep-alive': return None

    date = pre(msg['DATE'])

    print(date, color(36) + '%', color(245) + stripped + reset())

