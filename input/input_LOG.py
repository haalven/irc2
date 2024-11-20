

# handle user LOG

from time_calc import now


def handle(client, kb_args):

    if client.logfile:

        print( now() , '[LOG]' , '"' + client.logfile + '"' )

