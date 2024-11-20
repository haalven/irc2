

# handle PONG

from time_calc import pre, ts2dt
from xterm_control import bold,reset


def handle(client,msg):

    if len( msg['PAR'] ) > 0:

        for p in msg['PAR']:

            if p.startswith('time='):

                try:

                    ts = ts2dt(p.split('time=')[1])

                    rtt = msg['DATE'] - ts

                    ms  = round(rtt.total_seconds() * 1000)

                    print(pre(msg['DATE']), 'ping/pong roundtrip time:',
                          bold() + str(ms), 'millisec.' + reset())

                except Exception: pass

