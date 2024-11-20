

# display formatted messages

from time_calc import pre


def format(client,msg):

    # elements  (UnrealIRCd /MODULE)

    date   = pre( msg['DATE'] )

    info = '\x20'.join( msg['PAR'][1:] )


    # construct

    line = [ date , '[MODULE]' , info ]

    print( '\x20'.join(line) )

