

# handle 352 (RPL_WHOREPLY)

from copy import deepcopy


def handle(client, msg):

    if client.member_save:

        par = deepcopy( msg['PAR'] )

        channel, username, host, server, nick, flags, trailing = \
            par[1], par[2], par[3], par[4], par[5], par[6], par[7]

        hopcount, _, realname = trailing.partition('\x20')

        client.who_dict[nick] = (username,host,realname,server,flags)
