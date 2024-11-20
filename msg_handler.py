
# message handler

from handle import *


def msg_handler(client, msg):

    match msg['VERB']:

        case '001':             handle_001.handle(client,msg)
        case '004':             handle_004.handle(client,msg)
        case '005':             handle_005.handle(client,msg)
        case '311':             handle_311.handle(client,msg)
        case '314':             handle_311.handle(client,msg)
        case '315':             handle_315.handle(client,msg)
        case '318':             handle_318.handle(client,msg)
        case '322':             handle_322.handle(client,msg)
        case '323':             handle_323.handle(client,msg)
        case '352':             handle_352.handle(client,msg)
        case '353':             handle_353.handle(client,msg)
        case '366':             handle_366.handle(client,msg)
        case '369':             handle_318.handle(client,msg)
        case '381':             handle_381.handle(client,msg)
        case '433':             handle_433.handle(client,msg)
        case '903':             handle_903.handle(client,msg)
        case 'AUTHENTICATE':    handle_AUTH.handle(client,msg)
        case 'CAP':             handle_CAP.handle(client,msg)
        case 'ERROR':           handle_ERROR.handle(client,msg)
        case 'JOIN':            handle_JOIN.handle(client,msg)
        case 'KICK':            handle_KICK.handle(client,msg)
        case 'NICK':            handle_NICK.handle(client,msg)
        case 'NOTICE':          handle_NOTICE.handle(client,msg)
        case 'PART':            handle_PART.handle(client,msg)
        case 'PING':            handle_PING.handle(client,msg)
        case 'PONG':            handle_PONG.handle(client,msg)
        case 'PRIVMSG':         handle_PRIVMSG.handle(client,msg)
        case 'QUIT':            handle_QUIT.handle(client,msg)
        case 'RENAME':          handle_RENAME.handle(client,msg)

