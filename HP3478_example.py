from AR488 import AR488
from HP3478A import HP3478A
import time

interface = AR488('COM4')
meter = HP3478A(23,interface)

meter.address()
meter.print_message('AR488 minu')
time.sleep(3)
meter.normal_display()

while True:
    print(meter.get_measure())
    time.sleep(1)