

# handle 353 (RPL_NAMREPLY)

from copy import deepcopy


def handle(client,msg):

    chan  = deepcopy( msg['PAR'][2] )
    names = deepcopy( msg['PAR'][3] ) if len(msg['PAR'])>3 else ''
    members = names.split('\x20') if '\x20' in names else [names]


    # create names_dict[chan]
    if not (chan in client.names_dict): 
        client.names_dict[chan] = {}
 
        # add status-keys
        for status in client.chan_privs:
            client.names_dict[chan][client.chan_privs[status]] = []
        client.names_dict[chan]['user'] = []


    # fill names_dict
    for m in members:
        if not m.strip(): continue

        # privileged?
        if m[0] in client.chan_privs:
            client.names_dict[chan][client.chan_privs[m[0]]].append(m)
        else:
            client.names_dict[chan]['user'].append(m)

