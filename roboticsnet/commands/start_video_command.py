from roboticsnet.commands.commandable import Commandable

class StartVideoCommand(Commandable):
    """ Sends a request to boot the video process """

    def __init__(self, hooks):
        self.hooks = hooks

    def execute(self):
        self.hooks.startVideoHook()