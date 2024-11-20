
# global ignore mechanism
# NO logging, NO display, NO handling

from casemapping import casemapped


def ignore(client, msg):


    match msg['KEY']:

        # ignore `keep-alive` replies
        case 'PONG':
            if len( msg['PAR'] ) > 0:
                if msg['PAR'][-1] == 'keep-alive': return True


        # ignore @+typing TAGMSG
        case 'IS_TYPING': return True


        case 'PRIVMSG':

            # custom rules here

            return False


    return False
