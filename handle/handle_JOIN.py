

# handle JOIN

from copy import deepcopy
from casemapping import casemapped


def handle(client, msg):


    channel = deepcopy( msg['PAR'][0] )


    # YOU joined a channel

    if msg['KEY'] == 'YOU_JOIN':

        # track your channels

        if not (channel in client.mychans):

            client.mychans.append(channel)


    else:

        # channel defense, ops assumed
        # use profile[defchans] to enable
        # channel names must be casemapped

        if msg['BLACK']:

            if casemapped(client, channel) in client.profile['DEFCHANS']:

                banmask = '*!' + msg['ADDR']

                client.sock_send([ 'MODE' , channel , '+b' , banmask ])

                client.sock_send([ 'KICK' , channel , msg['NICK'] , 'auto-ban' ])
