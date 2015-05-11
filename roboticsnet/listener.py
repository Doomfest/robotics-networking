from roboticsnet.commands.move_command import MoveCommand

class Listener:
    """
    author: psyomn

    The listener is basically the main entry point for this smaller module
    for the rover. It is responsible for receiving information, and passing it
    first to the validator, and then to the dispatcher.
    """

    def __init__(self, default_port=5000):
        self.port = default_port

    def listen(self):
        """ main entry point """
        mv = MoveCommand(123)
        print "Listening on port: ", self.port
        mv.execute()
