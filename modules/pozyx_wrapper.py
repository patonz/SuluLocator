from pypozyx import PozyxSerial, DeviceRange, PozyxConstants, get_first_pozyx_serial_port, POZYX_SUCCESS

class PozyxWrapper:
    def __init__(self, anchors, callback=None):
        serial_port = get_first_pozyx_serial_port()
        if serial_port is None:
            raise Exception("No Pozyx connected. Check your USB cable or your driver!")
        self.pozyx = PozyxSerial(serial_port)
        self.anchors = anchors
        self.callback = callback

    def start(self):
        while True:
            for anchor in self.anchors:
                device_range = DeviceRange()
                status = self.pozyx.doRanging(anchor, device_range)
                if status == POZYX_SUCCESS:
                    if self.callback:
                        self.callback(anchor, device_range.distance)
