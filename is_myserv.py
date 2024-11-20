
# is my server?


def is_myserv(client, serv):


    serv = serv.strip().lower()

    myserv = client.myserv.lower()


    if serv == myserv: return True

    else: return False

