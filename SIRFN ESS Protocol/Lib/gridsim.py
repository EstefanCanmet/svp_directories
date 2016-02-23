import sys
import os
import glob
import importlib

# Import all gridsim extensions in current directory.
# A gridsim extension has a file name of gridsim_*.py and contains a function gridsim_params(info) that contains
# a dict with the following entries: name, init_func.

# dict of modules found, entries are: name : module_name

gridsim_modules = {}

def params(info):
    info.param_group('gridsim', label='Grid Simulator Parameters', glob=True)
    info.param('gridsim.mode', label='Mode', default='Manual', values=[])
    info.param('gridsim.auto_config', label='Configure grid simulator at beginning of test', default='Disabled',
               values=['Enabled', 'Disabled'])
    for mode, m in gridsim_modules.iteritems():
        m.params(info)

def gridsim_init(ts):
    """
    Function to create specific grid simulator implementation instances.

    Each supported grid simulator type should have an entry in the 'mode' parameter conditional.
    Module import for the simulator is done within the conditional so modules only need to be
    present if used.
    """
    mode = ts.param_value('gridsim.mode')
    sim_module = gridsim_modules.get(mode)
    if sim_module is not None:
        sim = sim_module.GridSim(ts)
    else:
        raise GridSimError('Unknown grid simulation mode: %s' % mode)

    return sim

REGEN_ON = 'on'
REGEN_OFF = 'off'
RELAY_OPEN = 'open'
RELAY_CLOSED = 'closed'
RELAY_UNKNOWN = 'unknown'

class GridSimError(Exception):
    """
    Exception to wrap all grid simulator generated exceptions.
    """
    pass


class GridSim(object):
    """
    Template for grid simulator implementations. This class can be used as a base class or
    independent grid simulator classes can be created containing the methods contained in this class.
    """

    def __init__(self, ts, params=None):
        self.ts = ts
        self.profile = []
        self.params = params

        if self.params is None:
            self.params = {}

    def config(self):
        """
        Perform any configuration for the simulation based on the previously
        provided parameters.
        """
        pass

    def open(self):
        """
        Open the communications resources associated with the grid simulator.
        """
        pass

    def close(self):
        """
        Close any open communications resources associated with the grid
        simulator.
        """
        pass

    def current_max(self, current=None):
        """
        Set the value for max current if provided. If none provided, obtains
        the value for max current.
        """
        if current is not None:
            pass
        else:
            current = 0.0
        return current

    def freq(self, freq=None):
        """
        Set the value for frequency if provided. If none provided, obtains
        the value for frequency.
        """
        if freq is not None:
            pass
        else:
            freq = 0.0
        return freq

    def profile_load(self, profile_name, v_step=100, f_step=100, t_step=None):
        """
        Load the profile either in list format or from a file.

        Each entry in the profile contains:
            time offset in seconds, voltage 1, voltage 2, voltage 3, frequency
        The voltage is applied to all phases.

        The profile param specifies the profile as a list of tuples in the form:
        (time, v1, v2, v3, frequency)

        The filename param specifies the profile as a csv file with the first
        line specifying the elements order of the elements and subsequent lines
        containing each profile entry:
        time, voltage 1, voltage 2, voltage 3, frequency
        t0, v1, v2, v3, f
        t1, v1, v2, v3, f
        """
        pass

    def profile_start(self):
        """
        Start the loaded profile.
        """
        pass

    def profile_stop(self):
        """
        Stop the running profile.
        """
        pass

    def regen(self, state=None):
        """
        Set the state of the regen mode if provided. Valid states are: REGEN_ON,
        REGEN_OFF. If none is provided, obtains the state of the regen mode.
        """
        if state is not None:
            pass
        else:
            state = REGEN_OFF
        return state

    def relay(self, state=None):
        """
        Set the state of the relay if provided. Valid states are: RELAY_OPEN,
        RELAY_CLOSED. If none is provided, obtains the state of the relay.
        """
        if state is not None:
            pass
        else:
            state = RELAY_OPEN
        return state

    def voltage(self, voltage=None):
        """
        Set the value for voltage 1, 2, 3 if provided. If none provided, obtains
        the value for voltage. Voltage is a tuple containing a voltage value for
        each phase.
        """
        if voltage is not None:
            pass
        else:
            voltage = (0.0, 0.0, 0.0)
        return voltage

    def voltage_max(self, voltage=None):
        """
        Set the value for max voltage if provided. If none provided, obtains
        the value for max voltage.
        """
        if voltage is not None:
            pass
        else:
            voltage = (0.0, 0.0, 0.0)
        return voltage

def gridsim_scan():
    global gridsim_modules
    # scan all files in current directory that match gridsim_*.py
    files = glob.glob(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'gridsim_*.py'))
    for f in files:
        module_name = None
        try:
            module_name = os.path.splitext(os.path.basename(f))[0]
            m = importlib.import_module(module_name)
            if hasattr(m, 'gridsim_info'):
                info = m.gridsim_info()
                mode = info.get('mode')
                # place module in module dict
                if mode is not None:
                    gridsim_modules[mode] = m
            else:
                if module_name is not None and module_name in sys.modules:
                    del sys.modules[module_name]
        except Exception, e:
            if module_name is not None and module_name in sys.modules:
                del sys.modules[module_name]
            raise GridSimError('Error scanning module %s: %s' % (module_name, str(e)))

# scan for gridsim modules on import
gridsim_scan()

if __name__ == "__main__":
    pass
