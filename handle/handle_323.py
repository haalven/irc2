

# handle 323 (RPL_LISTEND)

from time_calc import pre
from xterm_control import bold,light,reset


def handle(client,msg):

    if client.top_list  or client.save_list:

        date = pre( msg['DATE'] )

        # sort
        chans_sorted = dict( sorted(client.chan_dict.items(),
                            key=lambda item: item[1],
                            reverse=True) )
        client.chan_dict = {}

        # save list
        if client.save_list:
            network = client.isupport['NETWORK']
            site = network if network else client.myserv
            day = msg['DATE'].strftime('%y-%m-%d')
            listfile = client.ircpath + '/list/list_' + site + '_' + day + '.txt'
            with open(listfile, 'w') as f:
                for chan in chans_sorted:
                    count, topic = chans_sorted[chan]
                    line = [ chan , str(count) , topic ]
                    f.write( '\x20'.join(line) + '\n' )
            print( date , 'LIST' , 'saved .')

        # show top10
        chans_top  = {}
        for chan in chans_sorted:
            chans_top[chan] = chans_sorted[chan]
            if len(chans_top) >= 10: break
        verb = '[TOP10]'
        for chan in chans_top:
            count, topic = chans_top[chan]
            channel = bold() + chan + reset()
            topic   = light() + topic + reset()
            print( date , verb , channel , count , topic )


    client.top_list = False
    client.save_list = False
