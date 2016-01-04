from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.roboticsnet_exception import RoboticsnetException
import socket

class RoverClient:
    """
    The client that interfaces to the Rover gateway server. This is where we add
    different functions, that send the info to the server.

    author: psyomn
    """

    def __init__(self, host='localhost', port=ROBOTICSNET_PORT):
        self.host = host
        self.port = port

    def getPort(self):
        return self.port

    def getHost(self):
        return self.host

    def setHost(self, host):
        self.host = host

    def setPort(self, port):
        self.port = port


    def query(self):
        """ Issue a queryproc request """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_SYSTEM_QUERYPROC])
        return self._sendMessageAwaitReply(message)
        
    def sendCommand(self, command):
        """ Sends a request to the server """
        message = RoverUtils.hexArr2Str([command])
        self._sendMessage(message)
        
    def timedCommand(self, command, magnitude):
        """ Sends a request to the server """
        """ This is only for movement commands """
        self._validateByteValue(magnitude)
        message = RoverUtils.hexArrToTimestampedString([command, magnitude])
        self._sendMessage(message, False) #sent with udp

    def _sendMessage(self, message, TCP=True):
        """
        Given the host, and port, we build the connection. Don't call this
        outside the constructor, unless you know what you are doing.

        Parameters:
            message - is the bytearray to send, in string format
            TCP     - whether or not it will be sent with TCP. true by default
        """
        address = (self.host, self.port)
        if TCP:
            #from TCPCommunication on the Python wiki
            tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tsock.connect(address)
            tsock.send(message)
            tsock.close()
        else:
            #from UdpCommunication on the Python wiki
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message, address)

    def _sendMessageAwaitReply(self, message):
        """
        As _sendMessage, but this method waits for a reply

        Parameters:
            message - is the bytearray to send, in string format
        """
        address = (self.host, self.port)
        tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tsock.connect(address)
        tsock.send(message)
        data = tsock.recv(20)
        tsock.close()
        return data

    def sensInfo(self):
        """ Request information about sensors """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_SENSOR_INFO])
        return self._sendMessageAwaitReply(message)

    def _validateByteValue(self, value):
        """
        Check if value is between 0 to 255. If not, raise an exception

        Parameters:
            value - an integer.
        """
        if not value in range(0, 256):
            raise RoboticsnetException("You can send things in range of 0 to 255 only")
