from ppadb.client import Client

def connect_device():
    adb = Client()
    devices = adb.devices()

    if len(devices) == 0:
        print('No devices connected')
        quit()

    return devices[0]

device = connect_device()