
# display formatted messages

from re import search
from copy import deepcopy
from time_calc import pre

from format import *


def display_fmt(client, msg):

    # never display

    hide = ['007','017','018','219','235','262','272','315','318',
            '321','323','337','345','347','349','353','365','366',
            '368','369','374','376','394','607','697','701','703',
            '706','729','733','940','952','953']

    if msg['VERB'] in hide: return None


    # formatted output

    match msg['KEY']:

        case 'ACCOUNT':             format_ACCOUNT.format(client, msg); return
        case 'ACTION':              format_PRIVMSG.format(client, msg); return
        case 'ACT_AWAY':            format_ACT_AWAY.format(client, msg); return
        case 'ACT_BACK':            format_ACT_BACK.format(client, msg); return
        case 'ACT_JOIN':            format_ACT_JOIN.format(client, msg); return
        case 'ACT_NICK':            format_ACT_NICK.format(client, msg); return
        case 'ACT_PART':            format_ACT_PART.format(client, msg); return
        case 'ACT_QUIT':            format_ACT_QUIT.format(client, msg); return
        case 'AWAY':                return
        case 'BACK':                return
        case 'BATCH':               return
        case 'BATCH_BEGIN':         format_BATCH_BEGIN.format(client, msg); return
        case 'BATCH_END':           format_BATCH_END.format(client, msg); return
        case 'CAP':                 format_CAP.format(client, msg); return
        case 'CHAN_MODE':           format_CHAN_MODE.format(client, msg); return
        case 'CHAN_MODE_HL':        format_CHAN_MODE_HL.format(client, msg); return
        case 'CHANNEL_LIMIT':       format_CHANNEL_LIMIT.format(client, msg); return
        case 'CHGHOST':             format_CHGHOST.format(client, msg); return
        case 'CLEARCHAT':           format_CLEARCHAT.format(client, msg); return
        case 'CTCP':                format_CTCP.format(client, msg); return
        case 'ERR_BADCHANMASK':     format_ERR_ERROR.format(client, msg); return
        case 'ERR_BADCHANNELKEY':   format_ERR_ERROR.format(client, msg); return
        case 'ERR_BANNEDFROMCHAN':  format_ERR_ERROR.format(client, msg); return
        case 'ERR_CANNOTCHANGECHANMODE':format_ERR_ERROR.format(client, msg); return
        case 'ERR_CANNOTSENDTOCHAN':format_ERR_ERROR.format(client, msg); return
        case 'ERR_CHANNELISFULL':   format_ERR_ERROR.format(client, msg); return
        case 'ERR_CHANOPRIVSNEEDED':format_ERR_ERROR.format(client, msg); return
        case 'ERR_ERRONEUSNICKNAME':format_ERR_ERROR.format(client, msg); return
        case 'ERR_HELPNOTFOUND':    format_ERR_ERROR.format(client, msg); return
        case 'ERR_INPUTTOOLONG':    format_ERR_ERROR2.format(client, msg); return
        case 'ERR_INVALIDBAN':      format_ERR_ERROR.format(client, msg); return
        case 'ERR_INVALIDCAPCMD':   format_ERR_ERROR.format(client, msg); return
        case 'ERR_INVITEONLYCHAN':  format_ERR_ERROR.format(client, msg); return
        case 'ERR_MLOCKRESTRICTED': format_ERR_ERROR.format(client, msg); return
        case 'ERR_NEEDMOREPARAMS':  format_ERR_ERROR.format(client, msg); return
        case 'ERR_NEEDREGGEDNICK':  format_ERR_ERROR.format(client, msg); return
        case 'ERR_NICKNAMEINUSE':   format_ERR_ERROR.format(client, msg); return
        case 'ERR_NOPRIVILEGES':    format_ERR_ERROR2.format(client, msg); return
        case 'ERR_NOPRIVS':         format_ERR_ERROR.format(client, msg); return
        case 'ERR_NOSUCHCHANNEL':   format_ERR_ERROR.format(client, msg); return
        case 'ERR_NOSUCHNICK':      format_ERR_ERROR.format(client, msg); return
        case 'ERR_NOSUCHSERVER':    format_ERR_ERROR.format(client, msg); return
        case 'ERR_NOTONCHANNEL':    format_ERR_ERROR.format(client, msg); return
        case 'ERR_NOTREGISTERED':   format_ERR_ERROR2.format(client, msg); return
        case 'ERR_SASLFAIL':        format_ERR_SASLFAIL.format(client, msg); return
        case 'ERR_TOOMANYMATCHES':  format_ERR_ERROR.format(client, msg); return
        case 'ERR_UMODEUNKNOWNFLAG':format_ERR_ERROR2.format(client, msg); return
        case 'ERR_UNAVAILRESOURCE': format_ERR_ERROR.format(client, msg); return
        case 'ERR_UNKNOWNCOMMAND':  format_ERR_ERROR.format(client, msg); return
        case 'ERR_UNKNOWNMODE':     format_ERR_ERROR.format(client, msg); return
        case 'ERR_USERSDISABLED':   format_ERR_ERROR2.format(client, msg); return
        case 'ERR_WASNOSUCHNICK':   format_ERR_ERROR.format(client, msg); return
        case 'ERROR':               format_ERROR.format(client, msg); return
        case 'FAIL':                format_STD_REPLY.format(client, msg); return
        case 'FORCED_QUIT':         format_FORCED_QUIT.format(client, msg); return
        case 'GLOBAL':              format_GLOBAL.format(client, msg); return
        case 'HISTSERV':            format_HISTSERV.format(client, msg); return
        case 'INVITE':              format_INVITE.format(client, msg); return
        case 'IS_TYPING':           return
        case 'JOIN':                format_JOIN.format(client, msg); return
        case 'KICK':                format_KICK.format(client, msg); return
#        case 'KILL':                format_KILL.format(client, msg); return
#        case 'MODE':                format_MODE.format(client, msg); return
        case 'NICK':                format_NICK.format(client, msg); return
        case 'NOTE':                format_STD_REPLY.format(client, msg); return
        case 'NOTICE':              format_PRIVMSG.format(client, msg); return
        case 'PART':                format_PART.format(client, msg); return
        case 'PING':                format_PINGPONG.format(client, msg); return
        case 'PONG':                format_PINGPONG.format(client, msg); return
        case 'PRIVMSG':             format_PRIVMSG.format(client, msg); return
        case 'QUIT':                format_QUIT.format(client, msg); return
        case 'RENAME':              format_RENAME.format(client, msg); return
        case 'RPL_ADMINME':         format_RPL_ADMIN.format(client, msg); return
        case 'RPL_ADMINLOC1':       format_RPL_ADMIN.format(client, msg); return
        case 'RPL_ADMINLOC2':       format_RPL_ADMIN.format(client, msg); return
        case 'RPL_ADMINEMAIL':      format_RPL_ADMIN.format(client, msg); return
        case 'RPL_AWAY':            format_RPL_AWAY.format(client, msg); return
        case 'RPL_BANLIST':         format_RPL_BANLIST.format(client, msg); return
        case 'RPL_CHANNELMODEIS':   format_RPL_CHANNELMODEIS.format(client, msg); return
        case 'RPL_CHANNEL_URL':     format_RPL_CHANNEL_URL.format(client, msg); return
        case 'RPL_COMMANDS':        format_RPL_COMMANDS.format(client, msg); return
        case 'RPL_CREATED':         format_RPL_CREATED.format(client, msg); return
        case 'RPL_CREATIONTIME':    format_RPL_CREATIONTIME.format(client, msg); return
        case 'RPL_EXCEPTLIST':      format_RPL_BANLIST.format(client, msg); return
        case 'RPL_GLOBALUSERS':     format_RPL_LUSER.format(client, msg); return
        case 'RPL_HELLO':           format_RPL_HELLO.format(client, msg); return
        case 'RPL_HELPHDR':         format_RPL_HELPHDR.format(client, msg); return
        case 'RPL_HELPTLR':         format_RPL_HELPTLR.format(client, msg); return
        case 'RPL_HELPSTART':       format_RPL_HELPSTART.format(client, msg); return
        case 'RPL_HELPTXT':         format_RPL_HELPTXT.format(client, msg); return
        case 'RPL_INFO':            format_RPL_MOTD.format(client, msg); return
        case 'RPL_INVITING':        format_RPL_INVITING.format(client, msg); return
        case 'RPL_INVEXLIST':       format_RPL_BANLIST.format(client, msg); return
        case 'RPL_INVITELIST':      format_RPL_INVITELIST.format(client, msg); return
        case 'RPL_ISON':            format_RPL_ISON.format(client, msg); return
        case 'RPL_ISUPPORT':        format_RPL_ISUPPORT.format(client, msg); return
        case 'RPL_KNOCK':           format_RPL_KNOCK.format(client, msg); return
        case 'RPL_KNOCKDLVR':       format_RPL_KNOCKDLVR.format(client, msg); return
        case 'RPL_LANGUAGE':        format_RPL_LANGUAGE.format(client, msg); return
        case 'RPL_LINKS':           format_RPL_LINKS.format(client, msg); return
        case 'RPL_LIST':            format_RPL_LIST.format(client, msg); return
        case 'RPL_LOCALUSERS':      format_RPL_LUSER.format(client, msg); return
        case 'RPL_LOGGEDIN':        format_RPL_LOGGEDIN.format(client, msg); return
        case 'RPL_LOGGEDOUT':       format_RPL_LOGGEDOUT.format(client, msg); return
        case 'RPL_LOGON':           format_RPL_LOGON.format(client, msg); return
        case 'RPL_LOGOFF':          format_RPL_LOGOFF.format(client, msg); return
        case 'RPL_LUSERCHANNELS':   format_RPL_LUSER.format(client, msg); return
        case 'RPL_LUSERCLIENT':     format_RPL_LUSER.format(client, msg); return
        case 'RPL_LUSERME':         format_RPL_LUSER.format(client, msg); return
        case 'RPL_LUSEROP':         format_RPL_LUSER.format(client, msg); return
        case 'RPL_LUSERUNKNOWN':    format_RPL_LUSER.format(client, msg); return
        case 'RPL_MAP':             format_RPL_MAP.format(client, msg); return
        case 'RPL_MODLIST':         format_RPL_MODLIST.format(client, msg); return
        case 'RPL_MODLIST2':        format_RPL_MODLIST2.format(client, msg); return
        case 'RPL_MOTD':            format_RPL_MOTD.format(client, msg); return
        case 'RPL_MONONLINE':       format_RPL_MONONLINE.format(client, msg); return
        case 'RPL_MONOFFLINE':      format_RPL_MONOFFLINE.format(client, msg); return
        case 'RPL_MOTDSTART':       format_RPL_MOTDSTART.format(client, msg); return
        case 'RPL_MYINFO':          format_RPL_MYINFO.format(client, msg); return
        case 'RPL_NOTOPIC':         format_ERR_ERROR.format(client, msg); return
        case 'RPL_NOWAWAY':         format_RPL_NOWAWAY.format(client, msg); return
        case 'RPL_NOWOFF':          format_RPL_NOWOFF.format(client, msg); return
        case 'RPL_NOWON':           format_RPL_NOWON.format(client, msg); return
        case 'RPL_QUIETLIST':       format_RPL_BANLIST.format(client, msg); return
        case 'RPL_REMOTEISUPPORT':  format_RPL_ISUPPORT.format(client, msg); return
        case 'RPL_SASLSUCCESS':     format_RPL_SASLSUCCESS.format(client, msg); return
        case 'RPL_SERVLIST':        format_RPL_SERVLIST.format(client, msg); return
        case 'RPL_SILELIST':        format_RPL_SILELIST.format(client, msg); return
        case 'RPL_SNOMASK':         format_RPL_SNOMASK.format(client, msg); return
        case 'RPL_STATSCONN':       format_RPL_LUSER.format(client, msg); return
        case 'RPL_TOPIC':           format_RPL_TOPIC.format(client, msg); return
        case 'RPL_TOPICWHOTIME':    format_RPL_TOPICWHOTIME.format(client, msg); return
        case 'RPL_TRACELINK':       format_RPL_TRACELINK.format(client, msg); return
        case 'RPL_TRACEOPERATOR':   format_RPL_TRACEOPERATOR.format(client, msg); return
        case 'RPL_TRACESERVER':     format_RPL_TRACESERVER.format(client, msg); return
        case 'RPL_TRACEUSER':       format_RPL_TRACEUSER.format(client, msg); return
        case 'RPL_TRYAGAIN':        format_ERR_ERROR.format(client, msg); return
        case 'RPL_UMODEIS':         format_RPL_UMODEIS.format(client, msg); return
        case 'RPL_UNAWAY':          format_RPL_NOWAWAY.format(client, msg); return
        case 'RPL_USERHOST':        format_RPL_USERHOST.format(client, msg); return
        case 'RPL_VISIBLEHOST':     format_RPL_VISIBLEHOST.format(client, msg); return
        case 'RPL_WELCOME':         format_RPL_WELCOME.format(client, msg); return
        case 'RPL_WHOISACCOUNT':    format_RPL_WHOISACCOUNT.format(client, msg); return
        case 'RPL_WHOISCHANNELS':   format_RPL_WHOISCHANNELS.format(client, msg); return
        case 'RPL_WHOISIDLE':       format_RPL_WHOISIDLE.format(client, msg); return
        case 'RPL_WHOISSERVER':     format_RPL_WHOISSERVER.format(client, msg); return
        case 'RPL_WHOISUSER':       format_RPL_WHOISUSER.format(client, msg); return
        case 'RPL_WHOREPLY':        format_RPL_WHOREPLY.format(client, msg); return
        case 'RPL_WHOSPCRPL':       format_RPL_WHOXREPLY.format(client, msg); return
        case 'RPL_WHOWASUSER':      format_RPL_WHOISUSER.format(client, msg); return
        case 'RPL_YOUREOPER':       format_RPL_YOUREOPER.format(client, msg); return
        case 'RPL_YOURHOST':        format_RPL_YOURHOST.format(client, msg); return
        case 'SERV':                format_SERV.format(client, msg); return
        case 'SETNAME':             format_SETNAME.format(client, msg); return
        case 'SILENCE':             format_SILENCE.format(client, msg); return
        case 'SNO':                 format_SNO.format(client, msg); return
        case 'TAGMSG':              format_TAGMSG.format(client, msg); return
        case 'TOPIC':               format_TOPIC.format(client, msg); return
        case 'WALLOPS':             format_WALLOPS.format(client, msg); return
        case 'WARN':                format_STD_REPLY.format(client, msg); return
        case 'YOU_ACCOUNT':         format_YOU_ACCOUNT.format(client, msg); return
        case 'YOU_AWAY':            return  # depends on away-notify
        case 'YOU_BACK':            return  # depends on away-notify only
        case 'YOU_CHGHOST':         format_YOU_CHGHOST.format(client, msg); return
        case 'YOU_JOIN':            format_YOU_JOIN.format(client, msg); return
        case 'YOU_NICK':            format_YOU_NICK.format(client, msg); return
        case 'YOU_PART':            format_YOU_PART.format(client, msg); return
        case 'YOU_SETNAME':         format_YOU_SETNAME.format(client, msg); return
        case 'YOUR_INVITED':        format_YOUR_INVITED.format(client, msg); return
        case 'YOUR_KICKED':         format_YOUR_KICKED.format(client, msg); return
        case 'YOUR_KILLED':         format_YOUR_KILLED.format(client, msg); return
        case 'YOUR_MODE':           format_YOUR_MODE.format(client, msg); return



    # /WHOIS replies (311...318)

    if client.whoisreply:

        format_RPL_WHOIS.format(client, msg)

        return


    # display other/unknown msgs

    numeric = True if search(r'^\d\d\d', msg['VERB']) else False

    line = []

    line.append(pre(msg['DATE']))

    line.append(msg['KEY'])

    if numeric: line.append('(' + msg['VERB'] + ')')

    if not numeric: line.append(msg['NICK'])

    par = deepcopy(msg['PAR'])

    if numeric: par.pop(0)

    line.append('\x20'.join(par))


    line = list(filter(bool, line))

    print('\x20'.join(line))

