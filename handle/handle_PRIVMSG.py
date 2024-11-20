

# handle PRIVMSG

from is_active import update_active
from is_mynick import is_mynick

from handle.bot import *


def handle(client,msg):


    # skip chathistory
    if 'batch' in msg['TAGS']: return


    # update active nicks
    update_active(client, msg['NICK'], msg['DATE'])


    # real messages:
    if msg['KEY'] == 'PRIVMSG':


        # private message
        if is_mynick(client, msg['PAR'][0]):


            # remotebot commands
            if client.remotebot and msg['PAR'][1].startswith('!'):

                bot_cmd, _, bot_arg = msg['PAR'][1].partition('\x20')
                bot_cmd = bot_cmd.upper()

                # process
                match bot_cmd:
                    case '!AUTH':   bot_AUTH.handle(client,msg,bot_arg)
                    case '!ASCII':  bot_ASCII.handle(client,msg,bot_arg)
                    case '!BAN':    bot_BAN.handle(client,msg,bot_arg)
                    case '!CYCLE':  bot_CYCLE.handle(client,msg,bot_arg)
                    case '!DEAUTH': bot_DEAUTH.handle(client,msg,bot_arg)
                    case '!DO':     bot_DO.handle(client,msg,bot_arg)
                    case '!HELP':   bot_HELP.handle(client,msg,bot_arg)
                    case '!IN':     bot_IN.handle(client,msg,bot_arg)
                    case '!PARTALL':bot_PARTALL.handle(client,msg,bot_arg)
                    case '!SAY':    bot_SAY.handle(client,msg,bot_arg)
                    case '!STATUS': bot_STATUS.handle(client,msg,bot_arg)
                    case '!STOP':   bot_STOP.handle(client,msg,bot_arg)
                    case '!TIME':   bot_TIME.handle(client,msg,bot_arg)

