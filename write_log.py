
# write to logfile


def writelog(client, dt, logtxt):

    line = str(dt.timestamp()) + '\x20' + logtxt + '\n'

    with open(client.logfile, 'a') as f:

        f.write(line)
