from connect import device

def reset():
  device.shell('input tap 660 220')
  device.shell('input tap 630 250')

reset()