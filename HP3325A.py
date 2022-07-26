class HP3325A:
    """ module for controlling HP3325A from AR488 GPIb to USB adapter
    written by : Manuel Minutello

    INSTRUCTIONS :
    ->  before sending any command use address() to open device gpib address,
        otherwise the command might be sent to another instrument

    ->  use the functions to set up and read back the instrument"""
    # GPIB command on page 43 of manal

    _function = {
        'DC': '0',
        'sine': '1',
        'square': '2',
        'triangle': '3',
        'ramp_positive': '4',
        'ramp_negative': '5'
    }

    _sweep_mode = {
        'lin': '1',
        'log': '2'
    }

    _amp_units = {
        'V': 'VO',
        'mV': 'MV',
        'V_rms': 'VR',
        'mV_rms': 'MR',
        'dBm': 'DB'
    }

    _offset_units = {
        'V': 'VO',
        'mV': 'MV',
    }

    def __init__(self, gpib_id: int, interface, name='HP478A'):
        self.gpib_id = gpib_id
        self.interface = interface
        self.name = name

    def address(self):
        self.interface.cmd_set_address(self.gpib_id)

    def clear(self):
        self.interface.write('DCI')  # todo : test

    # internal command
    def constrain_com_len(self, val, limit, warn):
        val_str = str(val)
        error = False
        if val > 0:
            if len(val_str) > limit:
                val_str = val_str[:limit]
                error = True
        else:
            if len(val_str) > limit + 1:
                val_str = val_str[:limit + 1]
                error = True
        if error:
            raise Warning('{} too long "{}" -> constrained to {}'.format(warn, val, val_str))
        return val_str

    # commands
    def set_function(self, func):
        if func in self._function.keys():
            self.interface.write('FU{}'.format(self._function[func]))
        else:
            raise Exception('invalid mode "{}"'.format(func))

    def set_frequency(self, freq: float):
        freq_str = self.constrain_com_len(freq, 11, 'frequency')
        self.interface.write('FR {} HZ'.format(freq_str))  # also KH or MH valid

    def set_amplitude(self, amp: float, unit: str):
        if unit not in self._amp_units.keys():
            raise Exception('invalid amplitude unit "{}"'.format(unit))

        amp_str = self.constrain_com_len(amp, 4, 'amplitude')
        self.interface.write('AM {} {}'.format(amp_str, self._amp_units[unit]))

    def set_offset(self, offset: float, unit: str):
        if unit not in self._offset_units.keys():
            raise Exception('invalid offset unit "{}"'.format(unit))

        offset_str = self.constrain_com_len(offset, 4, 'offset')
        self.interface.write('OF {} {}'.format(offset_str, self._offset_units[unit]))

    def set_phase(self, phase: float):  # unit = deg
        phase_str = self.constrain_com_len(phase, 4, 'amplitude')
        self.interface.write('PH {} DE'.format(phase_str))

    def set_frequency_sweep(self, start_freq: float, stop_freq: float):
        start_freq_str = self.constrain_com_len(start_freq, 11, 'start_freq')
        self.interface.write('ST {} HZ'.format(start_freq_str))  # also KH or MH valid

        stop_freq_str = self.constrain_com_len(stop_freq, 11, 'stop_freq')
        self.interface.write('SP {} HZ'.format(stop_freq_str))  # also KH or MH valid

    def set_marker_frequency(self, freq):
        marker_str = self.constrain_com_len(freq, 11, 'marker_freq')
        self.interface.write('MF {} HZ'.format(marker_str))  # also KH or MH valid

    def set_sweep_time(self, time):
        time_str = self.constrain_com_len(time, 4, 'sweep time')
        self.interface.write('TI {} HZ'.format(time_str))  # also KH or MH valid

    def set_sweep_mode(self, mode: str):
        if mode not in self._sweep_mode.keys():
            raise Exception('invalid sweep mode "{}"'.format(mode))

        self.interface.write('SM {}'.format(self._sweep_mode[mode]))

    def enable_front_panel_output(self):
        self.interface.write('RF1')

    def enable_rear_panel_output(self):
        self.interface.write('RF2')

    def store_program(self, reg: int):
        if 0 <= reg <= 9:
            self.interface.write('SR {}'.format(reg))

    def recall_program(self, reg: int):
        if 0 <= reg <= 9:
            self.interface.write('RE {}'.format(reg))

    def set_phase_zero(self):
        self.interface.write('AP')

    def autocal(self):
        self.interface.write('AC')

    def start_single_sweep(self):
        self.interface.write('SS')

    def start_continuous_sweep(self):
        self.interface.write('SC')

    def self_test(self):
        self.interface.write('TE')

    def get_program_error(self):
        return self.interface.query('IER', expexted_payload = True)

    def get_frequency(self):
        return self.interface.query('IFR', expexted_payload = True)

    def get_amplitude(self):
        return self.interface.query('IAM', expexted_payload = True)

    def get_offset(self):
        return self.interface.query('IOF', expexted_payload = True)

    def get_phase(self):
        return self.interface.query('IPH', expexted_payload = True)

    def get_sweep_range(self):
        start = self.interface.query('IST', expexted_payload = True)
        stop = self.interface.query('ISP', expexted_payload = True)
        return start,stop

    def get_marker_freq(self):
        return self.interface.query('IMF', expexted_payload = True)

    def get_sweep_time(self):
        return self.interface.query('ITI', expexted_payload = True)

    def current_function(self):
        return self.interface.query('IFU', expexted_payload = True)

    def enable_hv_output(self, state = True):
        self.interface.write('HV {}'.format(1 if state else 0))

    def enable_am(self, state = True):
        self.interface.write('MA {}'.format(1 if state else 0))

    def enable_pm(self, state = True):
        self.interface.write('MP {}'.format(1 if state else 0))

