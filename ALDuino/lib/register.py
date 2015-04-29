"""register.py

Registers Naoqi service.
"""
import butane
import alduino


def main():
    """Register service."""
    butane.run_service(alduino.ALDuino)

if __name__ == '__main__':
    main()
