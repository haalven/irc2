
# reset client state

from time_calc import dt_now


def client_reset(client):

    client.connected    = False

    client.registered   = False

    client.opered       = False

    client.sasl_nick    = ''

    client.myserv       = ''

    client.mynick       = ''

    client.mychans      = []

    client.isupport     = {'NETWORK':''}

    client.usermodes    = ''

    client.svr_caps     = []

    client.active_caps  = []

    client.svr_version  = ''

    client.masters      = []

    client.active_nicks = {}

    client.lastmsg      = dt_now()

    client.blackdate    = dt_now()

    client.blackset     = set()

    client.whoisreply   = False

    client.top_list     = False

    client.save_list    = False

    client.chan_dict    = {}

    client.names_dict   = {}

    client.who_dict     = {}

    client.member_save  = False

    client.showparsed   = False

