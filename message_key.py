
# add key to msg

from copy import deepcopy
from forced_quit import forced_quit
from is_active import is_active
from is_tag import is_tag
from is_channel import is_channel
from is_mynick import is_mynick
from is_myserv import is_myserv
from listmodes import listmodes
from chan_privs import priv_modes


def message_key(client,msg):

    # fork verb => key
    key = deepcopy(msg['VERB'])


    # patch key
    match msg['VERB']:

        case '001': key = 'RPL_WELCOME'
        case '002': key = 'RPL_YOURHOST'
        case '003': key = 'RPL_CREATED'
        case '004': key = 'RPL_MYINFO'
        case '005': key = 'RPL_ISUPPORT'
        case '006': key = 'RPL_MAP'
        case '008': key = 'RPL_SNOMASK'
        case '015': key = 'RPL_MAP'
        case '020': key = 'RPL_HELLO'
        case '042': key = 'RPL_YOURID'
        case '105': key = 'RPL_REMOTEISUPPORT'
        case '200': key = 'RPL_TRACELINK'
        case '204': key = 'RPL_TRACEOPERATOR'
        case '205': key = 'RPL_TRACEUSER'
        case '206': key = 'RPL_TRACESERVER'
        case '221': key = 'RPL_UMODEIS'
        case '234': key = 'RPL_SERVLIST'
        case '250': key = 'RPL_STATSCONN'
        case '251': key = 'RPL_LUSERCLIENT'
        case '252': key = 'RPL_LUSEROP'
        case '253': key = 'RPL_LUSERUNKNOWN'
        case '254': key = 'RPL_LUSERCHANNELS'
        case '255': key = 'RPL_LUSERME'
        case '256': key = 'RPL_ADMINME'
        case '257': key = 'RPL_ADMINLOC1'
        case '258': key = 'RPL_ADMINLOC2'
        case '259': key = 'RPL_ADMINEMAIL'
        case '263': key = 'RPL_TRYAGAIN'
        case '265': key = 'RPL_LOCALUSERS'
        case '266': key = 'RPL_GLOBALUSERS'
        case '270': key = 'RPL_MAPUSERS'
        case '271': key = 'RPL_SILELIST'
        case '275': key = 'RPL_USINGSSL'
        case '290': key = 'RPL_HELPHDR'
        case '292': key = 'RPL_HELPTLR'
        case '294': key = 'RPL_HELPFWD'
        case '301': key = 'RPL_AWAY'
        case '302': key = 'RPL_USERHOST'
        case '303': key = 'RPL_ISON'
        case '304': key = 'RPL_MODLIST2'
        case '305': key = 'RPL_UNAWAY'
        case '306': key = 'RPL_NOWAWAY'
        case '307': key = 'RPL_WHOISREGNICK'
        case '311': key = 'RPL_WHOISUSER'
        case '312': key = 'RPL_WHOISSERVER'
        case '313': key = 'RPL_WHOISOPERATOR'
        case '314': key = 'RPL_WHOWASUSER'
        case '317': key = 'RPL_WHOISIDLE'
        case '319': key = 'RPL_WHOISCHANNELS'
        case '320': key = 'RPL_WHOISSPECIAL'
        case '322': key = 'RPL_LIST'
        case '324': key = 'RPL_CHANNELMODEIS'
        case '328': key = 'RPL_CHANNEL_URL'
        case '329': key = 'RPL_CREATIONTIME'
        case '330': key = 'RPL_WHOISACCOUNT'
        case '331': key = 'RPL_NOTOPIC'
        case '332': key = 'RPL_TOPIC'
        case '333': key = 'RPL_TOPICWHOTIME'
        case '335': key = 'RPL_WHOISBOT'
        case '336': key = 'RPL_INVITELIST'
        case '338': key = 'RPL_WHOISACTUALLY'
        case '341': key = 'RPL_INVITING'
        case '344': key = 'RPL_WHOISCOUNTRY'
        case '346':
            key = 'RPL_INVEXLIST'
            if not 'I' in listmodes(client): # undernet, quakenet
                key = 'RPL_INVITELIST'
        case '348': key = 'RPL_EXCEPTLIST'
        case '351': key = 'RPL_VERSION'
        case '352': key = 'RPL_WHOREPLY'
        case '353': key = 'RPL_NAMREPLY'
        case '354': key = 'RPL_WHOSPCRPL'
        case '364': key = 'RPL_LINKS'
        case '367': key = 'RPL_BANLIST'
        case '371': key = 'RPL_INFO'
        case '372': key = 'RPL_MOTD'
        case '375': key = 'RPL_MOTDSTART'
        case '378': key = 'RPL_WHOISHOST'
        case '381': key = 'RPL_YOUREOPER'
        case '391': key = 'RPL_TIME'
        case '396': key = 'RPL_VISIBLEHOST'
        case '401': key = 'ERR_NOSUCHNICK'
        case '402': key = 'ERR_NOSUCHSERVER'
        case '403': key = 'ERR_NOSUCHCHANNEL'
        case '404': key = 'ERR_CANNOTSENDTOCHAN'
        case '406': key = 'ERR_WASNOSUCHNICK'
        case '410': key = 'ERR_INVALIDCAPCMD'
        case '416': key = 'ERR_TOOMANYMATCHES'
        case '417': key = 'ERR_INPUTTOOLONG'
        case '421': key = 'ERR_UNKNOWNCOMMAND'
        case '422': key = 'ERR_NOMOTD'
        case '432': key = 'ERR_ERRONEUSNICKNAME'
        case '433': key = 'ERR_NICKNAMEINUSE'
        case '435': key = 'ERR_BANNICKCHANGE'
        case '436': key = 'ERR_NICKCOLLISION'
        case '437': key = 'ERR_UNAVAILRESOURCE'
        case '438': key = 'ERR_NICKTOOFAST'
        case '442': key = 'ERR_NOTONCHANNEL'
        case '443': key = 'ERR_USERONCHANNEL'
        case '446': key = 'ERR_USERSDISABLED'
        case '447': key = 'ERR_CANTCHANGENICK'
        case '451': key = 'ERR_NOTREGISTERED'
        case '461': key = 'ERR_NEEDMOREPARAMS'
        case '465': key = 'ERR_YOUREBANNEDCREEP'
        case '470': key = 'ERR_LINKCHANNEL'
        case '471': key = 'ERR_CHANNELISFULL'
        case '472': key = 'ERR_UNKNOWNMODE'
        case '473': key = 'ERR_INVITEONLYCHAN'
        case '474': key = 'ERR_BANNEDFROMCHAN'
        case '475': key = 'ERR_BADCHANNELKEY'
        case '476': key = 'ERR_BADCHANMASK'
        case '477': key = 'ERR_NEEDREGGEDNICK'
        case '479': key = 'ERR_BADCHANNAME'
        case '480': key = 'ERR_THROTTLE'
        case '481': key = 'ERR_NOPRIVILEGES'
        case '482': key = 'ERR_CHANOPRIVSNEEDED'
        case '501': key = 'ERR_UMODEUNKNOWNFLAG'
        case '524': key = 'ERR_HELPNOTFOUND'
        case '600': key = 'RPL_LOGON'
        case '601': key = 'RPL_LOGOFF'
        case '604': key = 'RPL_NOWON'
        case '605': key = 'RPL_NOWOFF'
        case '671': key = 'RPL_WHOISSECURE'
        case '687': key = 'RPL_LANGUAGE'
        case '698': key = 'ERR_LISTMODENOTSET'
        case '700': key = 'RPL_COMMANDS'
        case '702': key = 'RPL_MODLIST'
        case '704': key = 'RPL_HELPSTART'
        case '705': key = 'RPL_HELPTXT'
        case '710': key = 'RPL_KNOCK'
        case '711': key = 'RPL_KNOCKDLVR'
        case '723': key = 'ERR_NOPRIVS'
        case '728': key = 'RPL_QUIETLIST'
        case '730': key = 'RPL_MONONLINE'
        case '731': key = 'RPL_MONOFFLINE'
        case '732': key = 'RPL_MONLIST'
        case '740': key = 'RPL_RSACHALLENGE2'
        case '741': key = 'RPL_ENDOFRSACHALLENGE2'
        case '742': key = 'ERR_MLOCKRESTRICTED'
        case '743': key = 'ERR_INVALIDBAN'
        case '900': key = 'RPL_LOGGEDIN'
        case '901': key = 'RPL_LOGGEDOUT'
        case '903': key = 'RPL_SASLSUCCESS'
        case '904': key = 'ERR_SASLFAIL'
        case '906': key = 'ERR_SASLABORTED'
        case '926': key = 'ERR_BADCHANNEL'
        case '952': key = 'ERR_SILENCE'
        case '974': key = 'ERR_CANNOTCHANGECHANMODE'


        case 'ACCOUNT':
            if not client.registered: key = 'YOU_ACCOUNT'
            elif is_mynick(client, msg['NICK']):
                key = 'YOU_ACCOUNT'

        case 'AWAY':
            if not msg['PAR']: key = 'BACK'
            if is_mynick(client, msg['NICK']):
                key = 'YOU_' + key
            elif is_active(client,msg['NICK'], msg['DATE']):
                key = 'ACT_' + key

        case 'BATCH':
            if msg['PAR'][0].startswith('+'): key = 'BATCH_BEGIN'
            elif msg['PAR'][0].startswith('-'): key = 'BATCH_END'

        case 'CHGHOST':
            if not client.registered: key = 'YOU_CHGHOST'
            if is_mynick(client, msg['NICK']):
                key = 'YOU_CHGHOST'

        case 'INVITE':
            if is_mynick(client, msg['PAR'][0]):
                key = 'YOUR_INVITED'

        case 'JOIN':
            if is_mynick(client, msg['NICK']):
                key = 'YOU_JOIN'
            elif is_active(client, msg['NICK'], msg['DATE']): key = 'ACT_JOIN'

        case 'KICK':
            if is_mynick(client, msg['PAR'][1]):
                key = 'YOUR_KICKED'

        case 'KILL':
            if is_mynick(client, msg['PAR'][0]):
                key = 'YOUR_KILLED'

        case 'MODE':
            if is_mynick(client, msg['PAR'][0]):
                key = 'YOUR_MODE'
            elif is_channel(client, msg['PAR'][0]):
                key = 'CHAN_MODE'
                if msg['PAR'][1] == '+l': key = 'CHANNEL_LIMIT'
                if 'PREFIX' in client.isupport:
                    ignore = priv_modes(client) + 'l+-'
                else: ignore = 'qaohvl+-'
                for char in msg['PAR'][1]:
                    if not (char in ignore): key = 'CHAN_MODE_HL'
                if len(msg['PAR']) > 2:
                    for arg in msg['PAR'][2:]:
                        if is_mynick(client, arg):
                            key = 'CHAN_MODE_HL'

        case 'NICK':
            if is_mynick(client, msg['NICK']):
                key = 'YOU_NICK'
            elif is_active(client, msg['NICK'], msg['DATE']): key = 'ACT_NICK'

        case 'NOTICE':
            if not client.registered: key = 'SNO'
            elif is_myserv(client, msg['SRC']): key = 'SNO'
            elif (not msg['SRC']) and is_myserv(client, msg['PAR'][0]): key = 'SNO'
            elif msg['PAR'][0].startswith('$'): key = 'GLOBAL'
            # private
            elif is_mynick(client, msg['PAR'][0]):
                if (msg['SRC'] == client.profile['NICKSERV']) \
                or (msg['SRC'] == client.profile['CHANSERV']): key = 'SERV'

        case 'PART':
            if is_mynick(client, msg['NICK']):
                key = 'YOU_PART'
            elif is_active(client, msg['NICK'], msg['DATE']): key = 'ACT_PART'

        case 'PRIVMSG':
            if msg['PAR'][1].startswith('\x01'):
                ctcp_cmd, _, __ = msg['PAR'][1].strip('\x01').partition('\x20')
                key = 'ACTION' if ctcp_cmd == 'ACTION' else 'CTCP'
            elif (client.ircd_family == 'ergo') and (msg['NICK'] == 'HistServ'):
                key = 'HISTSERV'

        case 'QUIT':
            quitmsg = deepcopy(msg['PAR'][0]) if msg['PAR'] else ''
            if forced_quit(quitmsg): key = 'FORCED_QUIT'
            elif is_active(client, msg['NICK'], msg['DATE']): key = 'ACT_QUIT'

        case 'SETNAME':
            if is_mynick(client, msg['NICK']):
                key = 'YOU_SETNAME'

        case 'TAGMSG':
            if is_tag(msg, '+typing'): key = 'IS_TYPING'


    # add key to msg and return

    msg['KEY'] = key

    return msg

