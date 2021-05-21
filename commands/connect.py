from ppadb.client import Client

def __init__():
    adb = Client()
    devices = adb.devices()

    if len(devices) == 0:
        print('No devices connected')
        quit()

    return devices[0]

device = __init__()