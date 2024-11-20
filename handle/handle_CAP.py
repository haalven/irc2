

# handle CAP

from copy import deepcopy
from round_robin import round_robin

def handle(client, msg):


    # the CAP verb
    CAP_verb = deepcopy( msg['PAR'][1] ).upper()

    # parse CAP lists –> CAP_dict, CAP_list
    if CAP_verb in ['LS','NEW','DEL','ACK','NAK','LIST']:

        # multiline LS/LIST subcommand?
        multicap = False
        if ( CAP_verb in ['LS','LIST'] ) and ( msg['PAR'][2] == '*' ):
            msg['PAR'].pop(2)
            multicap = True

        # parse CAP_str
        CAP_str = deepcopy( msg['PAR'][2] ).strip()
        CAP_list = CAP_str.split('\x20') if '\x20' in CAP_str else [CAP_str]
        CAP_dict = {}
        for cap in CAP_list:
            capkey, _, capval = cap.partition('=')
            CAP_dict[capkey]  = capval
        CAP_list = list( CAP_dict )



    # now available CAPs
    if CAP_verb in ['LS', 'NEW']:

        # add to client.svr_caps
        for cap in CAP_list:
            if not cap in client.svr_caps: client.svr_caps.append(cap)


        if not multicap:  # -> CAP REQ

            # create REQ list
            reqlist = []
            for cap in client.svr_caps:
                realcap = cap.split('/')[-1] if '/' in cap else cap
                if realcap in client.client_caps:
                    reqlist.append(cap)

            # STOP: no hostname leaking
            if (CAP_verb=='LS') and client.profile['SASL_PWD'] and not ('sasl' in reqlist):
                print('PROBLEM:', 'server does not support SASL')
                round_robin(client)
                client.connection_reset()
                return None

            # send REQ
            if reqlist:
                client.sock_send( ['CAP', 'REQ', ':'+'\x20'.join(reqlist)] )
                client.svr_caps = []
            else:
                if not client.registered:
                    client.sock_send( ['CAP', 'END'] )  # no thanks


    # enabled CAPS -> sasl?
    elif CAP_verb == 'ACK':
        client.active_caps.extend(CAP_list)

        if ('sasl' in CAP_list) and client.profile['SASL_PWD']:
            client.sock_send(['AUTHENTICATE', 'PLAIN'])

        else:
            if not client.registered:
                client.sock_send(['CAP', 'END'])


    # delete CAPS
    elif CAP_verb == 'DEL':
        for cap in CAP_list:
            while cap in client.active_caps: client.active_caps.remove(cap)


    # list of active CAPs
    elif CAP_verb == 'LIST': client.active_caps = list(CAP_list)
