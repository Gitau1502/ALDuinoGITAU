"""arduino.py
NAOqi service that controls an Arduino board runnning the StandardFirmata
sketch.
"""
from time import sleep
from butane.fuel import Fuel
from pyfirmata import Arduino
from pyfirmata import util
from serial import SerialException


class ALDuino(Fuel):
    """ALDuino NAOqi service."""

    def __init__(self, session, path):
        super(ALDuino, self).__init__(session, path)
        self.board = None
        self.iter = None

    def connect_board(self, port):
        """Connect board in the given port."""
        try:
            self.board = Arduino(port)
            self.iter = util.Iterator(self.board)
            self.iter.start()
        except SerialException:
            return False
        return True

    def auto_connect_board(self):
        """Connect to an arduino board automatically by gessing its port to be
        /dev/ttyACM0 to /dev/ttyACM4.
        """
        for port_no in range(0, 5):
            success = self.connect_board('/dev/ttyACM{}'.format(port_no))
            if success:
                break
        return success

    def set_digital(self, pin_no, value):
        """Set the digital pin value.
        :param pin_no: integer pointing to the pin number.
        :param value: 0 or 1 corresponding to LOW and HIGH respectively.
        """

        pin_no = int(pin_no)
        value = int(value)
        if value > 0:
            self.board.digital[pin_no].write(1)
            return True
        else:
            self.board.digital[pin_no].write(0)
            return True

    def read_digital(self, pin_no):
        """Read digital pin state.
        :param pin_no: integer pointing to the pin number.
        :returns: 0 or 1"""
        pin_no = int(pin_no)
        return self.board.digital[pin_no].read()

    def read_analog(self, pin_no):
        """Read analog pin.
        :param pin_no: integer pointing to the pin number.
        :returns: float between 0 and 1 included.
        """
        pin_no = int(pin_no)
        self.board.analog[pin_no].enable_reporting()
        sleep(0.01)
        val = self.board.analog[pin_no].read()
        self.board.analog[pin_no].enable_reporting()
        return val
