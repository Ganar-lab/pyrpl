from ..lockbox import *
from ..signals import *


class InterferometerPort1(InputDirect):
    def expected_signal(self, phase):
        return self.mean + .5 * (self.max - self.min) * \
                           np.sin(phase)


class InterferometerPort2(InputDirect):
    def expected_signal(self, phase):
        return self.mean - .5 * (self.max - self.min) * \
                           np.sin(phase)


class Interferometer(Lockbox):
    _units = ['m', 'deg', 'rad']
    wavelength = FloatProperty(max=10000, min=0, default=1.064)
    _setup_attributes = ['wavelength']
    _gui_attributes = ['wavelength']
    variable = 'phase'

    inputs = LockboxModuleDictProperty(port1=InterferometerPort1,
                                            port2=InterferometerPort2)

    # pdh = InputPdh
    #    port1 = InterferometerPort1 # any attribute of type InputSignal will be instantiated in the model
    #    port2 = InterferometerPort2
    """
    @property
    def phase(self):
        if not hasattr(self, '_phase'):
            self._phase = 0
        return self._phase

    @phase.setter
    def phase(self, val):
        self._phase = val
        return val
    """

