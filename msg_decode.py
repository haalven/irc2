
# decode charset


def msg_decode(line):


    try: decoded = line.decode('utf-8')


    except UnicodeDecodeError:

        try: decoded = line.decode('latin-1')

        except UnicodeDecodeError:  return None

 
    badindex = decoded.find('\x00')

    if not badindex == -1: decoded = decoded[:badindex]


    return decoded
