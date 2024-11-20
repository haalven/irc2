
# input handler

from input import *


def cmd_handler(client, kb_in):


    # parse input

    if not kb_in: return

    if kb_in[0] == '@': kb_tags, _, kb_in = kb_in[1:].partition('\x20')
    else: kb_tags = ''

    kb_cmd, _, kb_arg = kb_in.partition('\x20')

    kb_cmd  =  kb_cmd.upper()

    kb_arg  =  kb_arg.replace('&me', client.mynick)

    kb_args =  kb_arg.split('\x20') if '\x20' in kb_arg else [kb_arg]


    # catch command

    match kb_cmd:

        case 'ABOUT':       input_WHOAMI.handle(client, kb_args); return
        case 'ACTION':      input_ACTION.handle(client, kb_args); return
        case 'ACTIVE':      input_ACTIVE.handle(client, kb_args); return
        case 'ASCII':       input_ASCII.handle(client, kb_args); return
        case 'BANLIST':     input_BANLIST.handle(client, kb_args); return
        case 'CAPS':        input_CAPS.handle(client, kb_args); return
        case 'CM':          input_CM.handle(client, kb_args); return
        case 'CMODE':       input_CMODES.handle(client, kb_args); return
        case 'CMODES':      input_CMODES.handle(client, kb_args); return
        case 'CTCP':        input_CTCP.handle(client, kb_args); return
        case 'CYCLE':       input_CYCLE.handle(client, kb_args); return
        case 'EXIT':        input_EXIT.handle(client, kb_args); return
        case 'EYES':        input_EYES.handle(client, kb_args); return
        case 'GLOBAL':      input_GLOBAL.handle(client, kb_args); return
        case 'HIST':        input_HIST.handle(client, kb_args); return
        case 'J':           input_JOIN.handle(client, kb_args); return
        case 'KEEPALIVE':   input_KEEPALIVE.handle(client, kb_args); return
        case 'LAG':         input_LAG.handle(client, kb_args); return
        case 'LISTMODES':   input_LISTMODES.handle(client, kb_args); return
        case 'LOG':         input_LOG.handle(client, kb_args); return
        case 'M':           input_MSG.handle(client, kb_args); return
        case 'ME':          input_ACTION.handle(client, kb_args); return
        case 'MEMBERS':     input_MEMBERS.handle(client, kb_args); return
        case 'MODULE':      input_MODULES.handle(client, ['MODULE',kb_args]); return
        case 'MODULES':     input_MODULES.handle(client, ['MODULES',kb_args]); return
        case 'MSG':         input_MSG.handle(client, kb_args); return
        case 'MYINFO':      input_WHOAMI.handle(client, kb_args); return
        case 'N':           input_NOTE.handle(client, kb_args); return
        case 'NOTE':        input_NOTE.handle(client, kb_args); return
        case 'PARSED':      input_PARSED.handle(client, kb_args); return
        case 'PARTALL':     input_PARTALL.handle(client, kb_args); return
        case 'PRIVS':       input_PRIVS.handle(client, kb_args); return
        case 'QUIT':        input_QUIT.handle(client, kb_args); return
        case 'RAW':         input_RAW.handle(client, kb_args); return
        case 'RSS':         input_RSS.handle(client, kb_args); return
        case 'SAVELIST':    input_SAVELIST.handle(client, kb_args); return
        case 'SHRUG':       input_SHRUG.handle(client, kb_args); return
        case 'SLAP':        input_SLAP.handle(client, kb_args); return
        case 'SYS':         input_SYS.handle(client, kb_args); return
        case 'TOP10':       input_TOP10.handle(client, kb_args); return
        case 'TRAFFIC':     input_TRAFFIC.handle(client, kb_args); return
        case 'UH':          input_UH.handle(client, kb_args); return
        case 'UMODE':       input_UMODES.handle(client, kb_args); return
        case 'UMODES':      input_UMODES.handle(client, kb_args); return
        case 'UPTIME':      input_UPTIME.handle(client, kb_args); return
        case 'W':           input_W.handle(client, kb_args); return
        case 'WHOAMI':      input_WHOAMI.handle(client, kb_args); return
        case 'WHOX':        input_WHOX.handle(client, kb_args); return
        case '?':           input_HELP.handle(client, kb_args); return


    # or pass

    line = [kb_cmd , kb_arg]

    if kb_tags: line.insert(0, '@' + kb_tags)

    client.sock_send('\x20'.join(line))

