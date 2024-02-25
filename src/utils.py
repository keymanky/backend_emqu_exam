import os

def pingE(host):
    try:
        response = os.system('ping -c 1 ' + host)
        if response == 0:
            return(1)
        else:
            return(0)

    except:
        return 0