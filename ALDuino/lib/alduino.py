"""arduino.py
NAOqi service that controls an Arduino board runnning the standard Firmatta
sketch.
"""

from butane.fuel import Fuel
from pyfirmata import Arduino
from serial import SerialException


class ALDuino(Fuel):
    """ALDuino NAOqi service."""

    def __init__(self, session, path):
        super(ALDuino, self).__init__(session, path)
        self.board = None

    def connect_board(self, port):
        """Connect board in the given port."""
        try:
            self.board = Arduino(port)
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

    def set_pin(self, pin_no, value):
        """Set the digital pin value"""

        pin_no = int(pin_no)
        value = int(value)
        if value > 0:
            self.board.digital[pin_no].write(1)
            return True
        else:
            self.board.digital[pin_no].write(0)
            return True
