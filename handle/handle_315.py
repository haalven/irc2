

# handle 315 (RPL_ENDOFWHO)

from membersave import membersave


def handle(client, msg):

    if client.member_save: membersave(client)

