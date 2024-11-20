
# CAP active ?


def real_cap(cap):

    return cap.split('/')[-1] if '/' in cap else cap


def is_cap(client, cap):

    for active in client.active_caps:

        if real_cap(cap.lower()) == real_cap(active.lower()):

            return True

    return False
