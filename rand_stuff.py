
# random stuff

from json import load
from random import choice
from text_lines import text_lines


# return a random nickname
def randnam(client):
    rndfile = client.ircpath + '/rndname.txt'
    return choice( text_lines(rndfile) )


# return a random number (string)
def randnum(digits):
    nums    = ['2','3','4','5','6','7','9']
    randnum = ''
    for i in range(digits): randnum += choice(nums)
    return randnum


# return a random quit msg
def randquit(client):
    quitfile = client.ircpath + '/quitmsg.json'
    with open(quitfile) as f: quits = load(f)
    return choice(quits)
