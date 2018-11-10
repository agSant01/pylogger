from pylogger.transporters.transporter import Transporter


class Console(Transporter):
    def transport(self, message):
        print(message)
