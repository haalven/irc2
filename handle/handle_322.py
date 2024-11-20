

# handle 322 (RPL_LIST)

from copy import deepcopy


def handle(client,msg):

    if client.top_list  or client.save_list:

        chan  = deepcopy( msg['PAR'][1] )

        count = int( deepcopy( msg['PAR'][2] ) )

        topic = deepcopy( msg['PAR'][3] ) if len(msg['PAR'])>3 else ''


        client.chan_dict[chan] = [ count, topic ]

