

# handle user UPTIME

from time_calc import dt_now, dt2ymd, td2str, pre


def handle(client, kb_args):

    date = dt_now()


    if client.connected:

        con_date  = dt2ymd(client.connected)

        con_delta = td2str(date - client.connected)

        print( pre(date) , '[uptime]' , 'connected at:' , con_date , '('+con_delta+')' )


    if client.registered:

        reg_date  = dt2ymd(client.registered)

        reg_delta = td2str(date - client.registered)

        print( pre(date) , '[uptime]' , 'registerd at:' , reg_date , '('+reg_delta+')' )

