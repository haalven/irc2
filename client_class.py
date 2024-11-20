
# ircclient class

from client_init     import client_init
from client_reset    import client_reset
from write_log       import writelog
from socksend        import socksend
from sockconnect     import sockconnect
from client_register import client_register
from sockread        import sockread
from msg_handler     import msg_handler
from cmd_handler     import cmd_handler


class IRCclient:

    def __init__(self, profile_name):

        # initialize the client
        client_init(self, profile_name)


    def connection_reset(self,):

        # kill connection
        self.ircsock.close()

        # reset client state
        client_reset(self)


    def sock_connect(self,):

        # kill connection and reset client
        self.connection_reset()

        # connect to server
        sockconnect(self)


    def sock_send(self, cmd):

        # send command to server
        socksend(self, cmd)


    def sock_read(self,):

        # read the socket and process lines
        sockread(self)


    def register(self,):

        # send registration data
        client_register(self)


    def msg_handle(self, msg):

        # handle server message
        msg_handler(self, msg)


    def user_cmd(self, kb_in):

        # handle user input
        cmd_handler(self, kb_in)


    def write_log(self, dt, logtxt):

        # log timestamp & message
        writelog(self, dt, logtxt)


