
# return the channel mode type (A,B,C,D)


def cmode_type(client, char):

    if not type(char) == str: return None

    if not char.isalpha(): return None

    if len(char) > 1: return None

    if not ('CHANMODES' in client.isupport): return None


    cmodes = client.isupport['CHANMODES'].split(',')

    if len (cmodes) < 4: return None

    A,B,C,D = cmodes[:4]

    if char in A: return 'A'
    if char in B: return 'B'
    if char in C: return 'C'
    if char in D: return 'D'

    return False
