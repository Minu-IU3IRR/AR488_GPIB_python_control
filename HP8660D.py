class HP8660D:
    """ module for controlling HP8660from AR488 GPIb to USB adapter (D version only)
        written by : Manuel Minutello

        INSTRUCTIONS :
        ->  before sending any command use address() to open device gpib address,
            otherwise the command might be sent to another instrument

        ->  use the functions to set up and read back the instrument"""

    def __init__(self, gpib_id: int, interface, name='HP8660D'):
        self.gpib_id = gpib_id
        self.interface = interface
        self.name = name

    def address(self):
        self.interface.cmd_set_address(self.gpib_id)

    # frequency control
    def set_center_frequency(self, frequency: int):
        self.interface.write('FR {} HZ'.format(frequency))

    def step_cf_up(self):
        self.interface.write('UP')

    def step_cf_down(self):
        self.interface.write('DN')

    def increment_set(self):
        self.interface.write('IS')

    # amplitude
    def set_output_level(self, level: float):
        self.interface.write('AP {}'.format(abs(level)) + '+dm' if level > 0 else '-dm')

    # modulation
    def set_fm_deviation(self, deviation: int):  # todo:testare per 3 digit?
        self.interface.write('FM {} HZ'.format(deviation))

    def set_am_depth(self, depth: float):
        if abs(depth) <= 100:
            depth = 100
        self.interface.write('AM {} PC'.format(abs(depth)))

    def set_phase_deviation(self, phase: int):
        self.interface.write('PM {} DG'.format(phase))

    def disable_modulation(self):
        self.interface.write('MO')

    def set_modulation_level(self, level):  # todo capire cosa è
        self.interface.write('PC {}'.format(level))

    def calibration_fm(self):
        self.interface.write('FC')

    # display
    def enable_display(self, state=True):
        self.interface.write('DO' if state else 'DB')

    def clear_register(self):
        self.interface.write('/')

    # modulation source
    def set_modulation_source(self, source):
        if source == 'internal_1kHz':
            self.interface.write('M1')
        elif source == 'internal_400Hz':
            self.interface.write('M2')
        elif source == 'internal_dc':
            self.interface.write('M4')
        elif source == 'external_ac':
            self.interface.write('M8')
        elif source == 'external_ac_unleveled':
            self.interface.write('M9')
        else:
            raise Exception('invalid modulation source "{}"'.format(source))

    # sweep
    def set_sweep_width(self, width):  # todo : testare, accetta input?
        self.interface.write('FS {}'.format(width))

    def set_sweep_mode(self, mode):
        if mode == 'auto':
            self.interface.write('W1')
        elif mode == 'single':
            self.interface.write('W2')
        elif mode == 'single_trigger':
            self.interface.write('W3')
        elif mode == 'off':
            self.interface.write('W0')
        else:
            raise Exception('invalid sweep mode "{}"'.format(mode))

    def set_sweep_rate(self, rate):
        if rate == 'slow':
            self.interface.write('T1')
        elif rate == 'med':
            self.interface.write('T2')
        elif rate == 'fast':
            self.interface.write('T3')
        else:
            raise Exception('invalid sweep rate "{}"'.format(rate))
