from pylogger.transporters.transporter import Transporter


class FileTransporter(Transporter):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def transport(self, message):
        f = open(self.filename, '+a')
        f.write(str(message) + '\n')
        f.close()
