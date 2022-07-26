from AR488 import AR488

interface = AR488('COM4', 115200, timeout=2)

# set interface lo listen only
interface.write('++mode 0')  # device mode
interface.write('++lon 1')  # listen only mode

while True:
    incoming = interface.read()
    if incoming != '':
        print('>>{}'.format(incoming))
