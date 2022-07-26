class HP3577A:
    """ module for controlling HP3577A from AR488 GPIb to USB adapter
        written by : Manuel Minutello

        INSTRUCTIONS :
        ->  before sending any command use address() to open device gpib address,
            otherwise the command might be sent to another instrument

        ->  use the functions to set up and read back the instrument"""

    # NOT IMPLEMENTED :
    # -> math functions in general, much faster to run on PC than instrument....
    # -> 'copy_scale': 'CPS',
    # -> 'polar_full_scale': 'PFS',
    # -> 'polar_phase_ref': 'PPR',
    # -> 'setting time entry' : 'STE'  # HPIB ony
    # -> 'dump state' : 'LMO'
    # -> 'load register' : 'LRx'
    # -> 'load state' : 'LMI'
    # -> 'data format' : 'FMx'
    # -> 'bus diagnostic' : 'BDx'
    # -> 'enter manu' : 'ENM'
    # -> 'enter graphics'
    # -> 'clear keyboard buffer'
    # -> 'set srq mask'
    # -> 'error reporting mode' : 'ERx'
    # -> 'send SRQ' : 'SRQ'
    #
    # # commands for opening menus on display (not implemented)
    # _menus = {
    #     'display': 'DSF*',
    #     'delay_aperture': 'DAP*',
    #     'return': 'RET*',
    #     'scale_menu': 'SCL*',
    #     'marker': 'MKR*',
    #     'sweep_type' : 'STY*',
    #     'sweep_mode' : 'SMD*',
    #     'sweep time' : 'STM*',
    #     'sweep_frequency' : 'FRQ*',
    #     'amplitude' : 'AMP*',
    #     'trigger_mode' : 'TRM*',
    #     'sweep resolution' : 'SRL*',
    #     'step sweep' : 'NST*',
    #     'resolution bandwidth' : 'RBW*',
    #     'average' : 'AVE*',
    #     'attenuation' : 'ATT*',
    #     'special functions' : 'SPC*',
    #     'confidence test' : 'SLF*',
    #     'service diagnostic' : 'SDG*',
    #     'more service diagnostic' : 'MOR*',
    #     'save instrument state' : 'SAV*',
    #     'recall instrument state' : 'RCL*',
    #     'plot' : 'PLM*',
    #     'configure plot' : 'CPT*',
    # }

    _span_aperture = {
        '0.5%': 'AP1',
        '1%': 'AP2',
        '2%': 'AP3',
        '4%': 'AP4',
        '8%': 'AP5',
        '16%': 'AP6',
    }

    _rapid_markers = {
        'reference_level': 'MTR',
        'start_frequency': 'MTA',
        'stop_frequency': 'MTB',
        'center_frequency': 'MTC',
        'min': 'MTN',
        'max': 'MTX',
        'full_scale': 'MTP',
        'polar_phase_ref': 'MPF'
    }

    _units = {
        'dBm': 'DBM',
        'dBv': 'DBV',
        'dB_rel': 'DBR',
        'V': 'V',
        'mV': 'MV',
        'uV': 'UV',
        'nV': 'NV',
        '°': 'DEG',
        '°/span': 'DSP',
        'rad': 'RAD',
        'rad/span': 'RSP',
        'S': 'SEC',
        'mS': 'MSC',
        'uS': 'USC',
        'nS': 'NSC',
        '%': '%',
        'MHz': 'MHZ',
        'kHz': 'KHZ',
        'Hz': 'HZ',
        '^': 'E',
        'm': 'MET',
        'cm': 'CM'
    }

    _sweep_type = {
        'linear': 'ST1',
        'alternate': 'ST2',
        'log': 'ST3',
        'amplitude': 'ST4',
        'cw': 'ST5',
        'discrete': 'ST6'
    }

    _sweep_mode = {
        'continuous': 'SM1',
        'single': 'SM2',
        'manual': 'SM3'
    }

    _sweep_resolution = {
        '51': 'RS1',
        '101': 'RS2',
        '201': 'RS3',
        '401': 'RS4',
    }

    _sweep_amp_step = {
        '6': 'NS1',
        '11': 'NS2',
        '21': 'NS3',
        '51': 'NS4',
        '101': 'NS5',
        '201': 'NS6',
        '401': 'NS7',
    }

    _trigger_modes = {
        'free_run': 'TG1',
        'line': 'TG2',
        'external': 'TG3',
        'immediate': 'TG4',
    }

    _resolution_bandwidth = {
        '1 Hz': 'BW1',
        '10 Hz': 'BW2',
        '100 Hz': 'BW3',
        '1 kHz': 'BW4',
    }

    _averaging = {
        'off': 'AV0',
        '4': 'AV1',
        '8': 'AV2',
        '16': 'AV3',
        '32': 'AV4',
        '64': 'AV5',
        '128': 'AV6',
        '256': 'AV7',
    }

    _attenuation = {
        'R0': 'AR1',
        'R20': 'AR2',

        'A0': 'AA1',
        'A20': 'AA2',

        'B0': 'AB1',
        'B20': 'AB2',
    }

    _impedance = {
        'R50': 'IR1',
        'R1M': 'IR2',

        'A50': 'IA1',
        'A1M': 'IA2',

        'B50': 'IB1',
        'B1M': 'IB2',
    }

    _length = {
        'R': 'LNR',
        'A': 'LNA',
        'B': 'LNB'
    }

    _inputs = {
        'R': 'INR',
        'A': 'INA',
        'B': 'INB',
        'A/R': 'A/R',
        'B/R': 'B/R',
        'D1': 'DI1',
        'D2': 'DI2',
        'D3': 'DI3',
        'D4': 'DI4',
        'user_defined': 'UDI'
    }

    _measurements = {
        'log_mag': 'DF7',
        'lin_mag': 'DF6',
        'phase': 'DF5',
        'polar': 'DF4',
        'real': 'DF3',
        'imaginary': 'DF2',
        'delay': 'DF1'
    }
    _s_measurements = {
        'S11': 'I11',
        'S21': 'I21',
        'S12': 'I12',
        'S22': 'I22'
    }

    def __init__(self, gpib_id: int, interface, name='HP3577A'):
        self.gpib_id = gpib_id
        self.interface = interface
        self.name = name

    def address(self):
        self.interface.cmd_set_address(self.gpib_id)

    def set_local(self):
        self.interface.write('DCL')

    def clear(self):
        self.interface.write('GTL')

    def select_input(self, channel: str):
        if channel in self._inputs.keys():
            self.interface.write(self._inputs[channel])
        else:
            raise Exception('invalid input "{}"'.format(channel))

    def select_s_measurement(self, s_measurement: str):
        if s_measurement in self._s_measurements.keys():
            self.interface.write(self._s_measurements[s_measurement])
        else:
            raise Exception('invalid S measurement "{}"'.format(s_measurement))

    def enable_s_param(self, state: bool):
        self.interface.write('SP1' if state else 'SP0')

    def select_measurement(self, measurement: str):
        if measurement in self._measurements.keys():
            self.interface.write(self._measurements[measurement])
        else:
            raise Exception('invalid measurement "{}"'.format(measurement))

    def enable_smith_chart(self, state: bool):
        self.interface.write('GT1' if state else 'GT0')

    def trace_off(self):
        self.interface.write('DF0')

    def test_set_direction(self, direction: str):
        if direction == 'forward':
            self.interface.write('TSF')
        elif direction == 'reverse':
            self.interface.write('TSR')
        else:
            raise Exception('invalid direction "{}"'.format(direction))

    def select_trace(self, trace: int):
        if trace == 1:
            self.interface.write('TR1')
        elif trace == 2:
            self.interface.write('TR2')
        else:
            raise Exception('invalid trace "{}"'.format(trace))

    # scale
    def autoscale(self):
        self.interface.write('ASL')

    def set_scale(self, val, unit):
        self._run_if_valid_unit('DIV', val, unit)

    # reference line
    def set_reference_level(self, val, unit):
        self._run_if_valid_unit('REF', val, unit)

    def set_reference_pos(self, val, unit):
        self._run_if_valid_unit('RPS', val, unit)

    def enable_reference_line(self, state):
        self.interface.write('RL1' if state else 'RL0')

    # phase slope
    def set_phase_slope(self, val, unit):
        self._run_if_valid_unit('PSL', val, unit)

    def enable_phase_slope(self, state):
        self.interface.write('PS1' if state else 'PS0')

    # marker
    def set_marker_position(self, val, unit):
        self._run_if_valid_unit('MKP', val, unit)

    def enable_marker(self, state):
        self.interface.write('MR1' if state else 'MR0')

    def zero_marker(self):
        self.interface.write('ZMK')

    # marker offset
    def enable_marker_offset(self, state: bool):
        self.interface.write('MO1' if state else 'MO0')

    def set_marker_offset(self, val, unit):
        self._run_if_valid_unit('MKO', val, unit)

    def set_marker_offset_frequency(self, val, unit):
        self._run_if_valid_unit('MOF', val, unit)

    def set_marker_offset_amplitude(self, val, unit):
        self._run_if_valid_unit('MOA', val, unit)

    def enable_marker_coupling(self, state):
        self.interface.write('CO1' if state else 'CO0')

    # polar graph control
    def set_polar_mag_offset(self, val, unit):
        self._run_if_valid_unit('PMO', val, unit)

    def set_polar_phase_offset(self, val, unit):
        self._run_if_valid_unit('PPO', val, unit)

    def set_polar_real_offset(self, val, unit):
        self._run_if_valid_unit('PRO', val, unit)

    def set_polar_img_offset(self, val, unit):
        self._run_if_valid_unit('PIO', val, unit)

    def set_polar_marker_units_re_img(self, val, unit):
        self._run_if_valid_unit('MRI', val, unit)

    def set_polar_marker_units_mg_ph(self, val, unit):
        self._run_if_valid_unit('MMP', val, unit)

    # quick markers
    def set_quick_marker(self, marker_type):
        if marker_type in self._rapid_markers.keys():
            self.interface.write(self._rapid_markers[marker_type])

    def set_marker_offset_to_span(self):
        self.interface.write('MOS')

    def set_marker_target(self, val, unit):
        self._run_if_valid_unit('MTV', val, unit)

    def move_market_target_left(self):
        self.interface.write('MLT')

    def move_marker_target_right(self):
        self.interface.write('MRT')

    # data storage
    def store(self, register: int):
        if 1 <= register <= 4:
            self.interface.write('SD{}'.format(register))
        else:
            raise Exception('invalid register number  "{}"'.format(register))

    def store_and_display(self):
        self.interface.write('STD')

    def store_user_defined(self):
        self.interface.write('UDS')

    def move_stored_data_to(self, register):
        if 1 <= register <= 4:
            self.interface.write('TD{}'.format(register))
        else:
            raise Exception('invalid register number  "{}"'.format(register))

    # calibration
    def normalize(self):
        self.interface.write('NRM')

    def normalize_short(self):
        self.interface.write('NRS')

    def cal_partial(self):
        self.interface.write('CPR')

    def cal_full(self):
        self.interface.write('CFL')

    def cal_continue(self):
        self.interface.write('CGO')

    # panel controls
    def arrow_up(self):
        self.interface.write('IUP')

    def arrow_down(self):
        self.interface.write('IDN')

    def enable_knob(self, state):
        self.interface.write('CE1' if state else 'CE0')

    def entry_off(self):
        self.interface.write('HLD')

    # delay aperture control
    def set_span_aperture(self, aperture):
        if aperture in self._span_aperture.keys():
            self.interface.write(self._span_aperture[aperture])
        else:
            raise Exception('invalid delay aperture "{}"'.format(aperture))

    # source control
    def set_sweep_type(self, mode):
        if mode in self._sweep_type.keys():
            self.interface.write(self._sweep_type[mode])
        else:
            raise Exception('invalid sweep type "{}"'.format(mode))

    def set_sweep_direction(self, direction):
        if direction == 'up':
            self.interface.write('SUP')
        elif direction == 'down':
            self.interface.write('SDN')
        else:
            raise Exception('invalid direction "{}"'.format(direction))

    def set_sweep_mode(self, mode):
        if mode in self._sweep_mode.keys():
            self.interface.write(self._sweep_mode[mode])
        else:
            raise Exception('invalid sweep mode "{}"'.format(mode))

    def set_sweep_time(self, val, unit):
        self._run_if_valid_unit('SWT', val, unit)

    def set_step_time(self, val, unit):
        self._run_if_valid_unit('SMT', val, unit)

    def set_sample_time(self, val, unit):
        self._run_if_valid_unit('MSR', val, unit)

    def set_source_frequency(self, val, unit):
        self._run_if_valid_unit('SFR', val, unit)

    def set_start_frequency(self, val, unit):
        self._run_if_valid_unit('FRA', val, unit)

    def set_stop_frequency(self, val, unit):
        self._run_if_valid_unit('FRB', val, unit)

    def set_center_frequency(self, val, unit):
        self._run_if_valid_unit('FRC', val, unit)

    def set_span_frequency(self, val, unit):
        self._run_if_valid_unit('FRS', val, unit)

    def set_frc_step_size(self, val):
        self.interface.write('CFS {}'.format(val))

    def set_sweep_resolution(self, val):
        if val in self._sweep_resolution.keys():
            self.interface.write(self._sweep_resolution[val])
        else:
            raise Exception('invalid sweep resolution "{}"'.format(val))

    def set_full_sweep(self):
        self.interface.write('FSW')

    def set_frequency_step_size(self, val, unit):
        self._run_if_valid_unit('FST', val, unit)

    # amplitude control
    def set_source_amplitude(self, val, unit):
        self._run_if_valid_unit('SAM', val, unit)

    def set_amplitude_step_size(self, unit, val):
        self._run_if_valid_unit('AST', val, unit)

    def clear_source_trip(self):
        self.interface.write('CTS')

    def set_start_amplitude(self, unit, val):
        self._run_if_valid_unit('AMA', val, unit)

    def set_stop_amplitude(self, unit, val):
        self._run_if_valid_unit('AMB', val, unit)

    def set_amplitude_step(self, val):
        if val in self._sweep_amp_step.keys():
            self.interface.write(self._sweep_amp_step[val])
        else:
            raise Exception('invalid amplitude step "{}"'.format(val))

    # trigger
    def set_trigger_mode(self, val):
        if val in self._trigger_modes.keys():
            self.interface.write(self._trigger_modes[val])
        else:
            raise Exception('invalid trigger mode "{}"'.format(val))

    # receiver
    def ser_resolution_bandwidth(self, val):
        if val in self._resolution_bandwidth.keys():
            self.interface.write(self._resolution_bandwidth[val])
        else:
            raise Exception('invalid resolution bandwidth "{}"'.format(val))

    def enable_auto_bandwidth(self, state: bool):
        self.interface.write('AU1' if state else 'AU0')

    def set_averaging(self, val):
        if type(val) == int:
            val = str(val)

        if val in self._averaging.keys():
            self.interface.write(self._averaging[val])
        else:
            raise Exception('invalid average "{}"'.format(val))

    def set_channel_attenuation(self, channel, val):
        if type(val) == int:
            val = str(val)
        if channel in ('A', 'B', 'R'):
            if val in ('0', '20'):
                key = channel + str(val)
                if key in self._attenuation.keys():
                    self.interface.write(self._impedance[key])
                else:
                    raise Exception('error in setting attenuation key')
            else:
                raise Exception('invalid attenuation value "{}"'.format(val))
        else:
            raise Exception('invalid channel "{}"'.format(channel))

    def set_channel_impedance(self, channel: str, val):
        if type(val) == int:
            val = str(val)
        if channel in ('A', 'B', 'R') and (val == '1M' or val == '50'):
            key = channel + str(val)
            if key in self._impedance.keys():
                self.interface.write(self._impedance[key])
        else:
            raise Exception('invalid channel "{}" impedance "{}"'.format(channel, val))

    def receiver_clear_trip(self):
        self.interface.write('CRT')

    # length
    def set_chanel_length(self, channel, val, unit):
        if channel in self._length.keys():
            self._run_if_valid_unit(self._length[channel], val, unit)
        else:
            raise Exception('invalid channel "{}"'.format(channel))

    def enable_channel_length(self, channel, state: bool):
        if channel == 'A':
            self.interface.write('LA1' if state else 'LA0')
        elif channel == 'B':
            self.interface.write('LB1' if state else 'LB0')
        elif channel == 'R':
            self.interface.write('LR1' if state else 'LR0')
        else:
            raise Exception('invalid channel "{}"'.format(channel))

    # diagnostic
    def run_channel_confidence_check(self, channel):
        if channel == 'A':
            self.interface.write('STA')
        elif channel == 'B':
            self.interface.write('STB')
        elif channel == 'R':
            self.interface.write('STR')
        else:
            raise Exception('invalid channel "{}"'.format(channel))

    def enable_beeper(self, state: bool):
        self.interface.write('BP1' if state else 'BP0')

    def enable_source_leveling(self, state: bool):
        self.interface.write('SL1' if state else 'SL0')

    def enable_setting_time(self, state: bool):
        self.interface.write('SE1' if state else 'SE0')

    def enable_synthesizer_diagnostics(self, state: bool):
        self.interface.write('SY1' if state else 'SY0')

    def test_display_pattern(self):
        self.interface.write('DTP')

    def test_trace_mem(self):
        self.interface.write('DTP')

    def test_fast_processor(self):
        self.interface.write('FPT')

    def test_io(self):
        self.interface.write('PRT')

    def test_display_mem(self):
        self.interface.write('DST')

    def software_revision_message(self):
        self.interface.write('SRV')

    def save_instrument_state_in_reg(self, reg: int):
        if 1 <= reg <= 5:
            self.interface.write('SV{}'.format(reg))
        else:
            raise Exception('invalid resister "{}"'.format(reg))

    def recall_instrument_state_from_reg(self, reg: int):
        if 1 <= reg <= 5:
            self.interface.write('RC{}'.format(reg))
        else:
            raise Exception('invalid register "{}"'.format(reg))

    def preset(self):
        self.interface.write('IPR')

    # plot
    def plot_all(self):
        return self.interface.write('PLA', response_payload=True)

    def plot_trace(self, trace: int):
        if 1 <= trace <= 2:
            return self.interface.write('PL{}'.format(trace), response_payload=True)
        else:
            raise Exception('invalid trace "{}"'.format(trace))

    def plot_graticule(self):
        return self.interface.write('PLG', response_payload=True)

    def plot_characteristic(self):
        return self.interface.write('PLC', response_payload=True)

    def plot_trace_marker(self, trace: int):
        if 1 <= trace <= 2:
            return self.interface.write('PM{}'.format(trace), response_payload=True)
        else:
            raise Exception('invalid trace "{}"'.format(trace))

    def set_trace_line_type(self, trace: int, line_type):
        if 1 <= trace <= 2:
            self.interface.write('T{}L {}'.format(trace, line_type))
        else:
            raise Exception('invalid trace "{}"'.format(trace))

    def set_trace_pen_number(self, trace: int, pen_number):
        if 1 <= trace <= 2:
            self.interface.write('T{}P {}'.format(trace, pen_number))
        else:
            raise Exception('invalid trace "{}"'.format(trace))

    def set_graticolate_pen(self, pen):
        self.interface.write('PGP {}'.format(pen))

    def set_pen_speed_fast(self, fast: bool):
        self.interface.write('PNM' if fast else 'PNS')

    def plot_reset_config(self):
        self.interface.write('PLD')

    def set_plotter_address(self, addr: int):
        if 0 <= addr <= 30:
            self.interface.write('HPB {}'.format(addr))
        else:
            raise Exception('invalid GPIB address "{}"'.format(addr))

    # HPIB only commands

    def dump_register(self, reg: str):
        if reg in ('A', 'B', 'R', 'D1', 'D2', 'D3', 'D4'):
            return self.interface.write('DD{}'.format(reg), response_payload=True)
        else:
            raise Exception('invalid trace "{}"'.format(reg))

    def dump_trace(self, trace: int):
        if 1 <= trace <= 2:
            return self.interface.write('DT{}'.format(trace), response_payload=True)
        else:
            raise Exception('invalid trace "{}"'.format(trace))

    def dump_marker(self, marker):
        if 1 <= marker <= 2:
            return self.interface.write('DM{}'.format(marker), response_payload=True)
        else:
            raise Exception('invalid marker "{}"'.format(marker))

    def dump_marker_pos(self, marker_pos):
        if 1 <= marker_pos <= 2:
            return self.interface.write('DM{}'.format(marker_pos), response_payload=True)
        else:
            raise Exception('invalid marker "{}"'.format(marker_pos))

    def dump_status(self):
        return self.interface.write('DMS', response_payload=True)

    def dump_average_num(self):
        return self.interface.write('DAN', response_payload=True)

    def dump_key_knob(self):
        return self.interface.write('DKY', response_payload=True)

    def dump_characteristic(self):
        return self.interface.write('DCH', response_payload=True)

    def get_id(self):
        return self.interface.write('ID?', response_payload=True)

    def enable_graticule(self, state: bool):
        self.interface.write('GR1' if state else 'GR0')

    def enable_characters(self, state: bool):
        self.interface.write('CH1' if state else 'CH0')

    def enable_annotation(self, state: bool):
        self.interface.write('AN1' if state else 'AN0')

    def clear_annotation(self):
        self.interface.write('ANC')

    def enable_menu(self, state: bool):
        self.interface.write('MN1' if state else 'MN0')

    def take_measurement(self):  # todo : verificare se ha payload
        self.interface.write('TKM')

    # -------------------------
    def _run_if_valid_unit(self, command, value, unit):
        if unit in self._units.keys():
            self.interface.write('{} {} {}'.format(command, value, self._units[unit]))
        else:
            raise Exception(' unit {} invalid'.format(unit))
