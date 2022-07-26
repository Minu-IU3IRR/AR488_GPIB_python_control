class HP3478A:
    """ module for controlling HP3578A from AR488 GPIb to USB adapter
    written by : Manuel Minutello

    INSTRUCTIONS :
    ->  before sending any command use address() to open device gpib address,
        otherwise the command might be sent to another instrument

    ->  use the functions to set up and read back the instrument"""

    _function = {
        'DC-V': 'F1',
        'DC-I': 'F5',
        'AC-V': 'F2',
        'AC-I': 'F6',
        'RES-2W': 'F3',
        'RES-4W': 'F4'
    }
    _range = {
        # todo
    }

    _digits = {
        '3.5': 'N3',
        '4.5': 'N4',
        '5.5': 'N5'
    }

    _trigger = {
        'internal': 'T1',
        'external': 'T2',
        'single': 'T3',
        'hold': 'T4',
        'fast': 'T5'
    }
    _auto_zero = {
        'on': 'Z0',
        'off': 'Z1'
    }

    _preset = {
        'home': 'H0'
        # todo
    }

    def __init__(self, gpib_id, interface, name='HP478A'):
        self.gpib_id = gpib_id
        self.interface = interface
        self.name = name

    def address(self):
        self.interface.cmd_set_address(self.gpib_id)

    # measurement control
    def set_function(self, new_function):
        if new_function in self._function.keys():
            self.interface.write(self._range[new_function])
            return True
        return False

    def set_range(self, new_range):
        if new_range in self._range.keys():
            self.interface.write(self._range[new_range])
            return True
        return False

    def set_digits(self, new_digits):
        if new_digits in self._digits.keys():
            self.interface.write(self._digits[new_digits])
            return True
        return False

    def set_trigger(self, new_trigger):
        if new_trigger in self._trigger.keys():
            self.interface.write(self._trigger[new_trigger])
            return True
        return False

    def set_auto_zero(self, new_status):
        if new_status:
            self.interface.write("Z1")
        else:
            self.interface.write("Z0")

    def preset(self, new_preset):
        if new_preset in self._preset.keys():
            self.interface.write(self._preset[new_preset])
            return True
        return False

    def enable_autorange(self):
        self.interface.write('RA')

    # get_data
    def get_measure(self):
        return self.interface.cmd_read()

    def get_status(self):
        return self.interface.query('B',response_payload=True)

    def get_errors(self):
        return self.interface.query('E',response_payload=True)

    def get_fr_switch_sate(self):
        return self.interface.query('S',response_payload=True)

    # screen control
    def print_message(self, message: str):
        self.interface.write('D2{}'.format(message.upper()))

    def normal_display(self):
        self.interface.write('D1')

    # read cal data ( WARNING!!!!! : experimental, make sure cal key is horizontal for cal lock)
    # def get_cal_nibble(self, addr:int):
    #     if 0 <= addr <= 255:
    #         raise Exception('error on getting cal nibble, 255 addresses only!, queried {}'.format(addr))
    #     else:
    #         #todo : implementare offset 0x40
    #         return self.interface.query('W{}'.format(addr), response_payload=True)[0]
    #
    # def get_cal_memory(self):
    #     dump = ''
    #     for i in range(247):
    #         dump = dump + self.get_cal_nibble(i)
    #     return dump