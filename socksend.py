
# send command to server

from strip_codes import strip_codes
from msg_parser import msg_parser
from time_calc import dt_now
from display_send import display_send
from xterm_control import color, light, reset


def socksend(client, cmd):

    if client.connected:

        line = '\x20'.join(cmd) if type(cmd) == list else str(cmd)

        stripped = strip_codes(line)

        outgoing = stripped + '\r\n'

        msg = msg_parser(stripped)

        msg['DATE'] = dt_now()


        # check
        if len(outgoing) > 512:
            print(color(196) + 'FAILED:', 'message too long',
                '(not sent):' + reset(), light() + stripped + reset())
            return None

        # send
        try: client.ircsock.sendall(outgoing.encode('utf-8'))
        except Exception as e:
            print('WRITE ERROR:', str(e))
            return None

        # log
        client.write_log(msg['DATE'], ':' + chr(10024) + '\x20' + stripped)


        # display
        if not client.hide_send: display_send(client, msg, stripped)

