"""
author: psyomn

This will take in the string that is sent to the networking gateway, and
check if it's in understandable format. Any checks should be done in this
file for now
"""

def validate(cmd_str):
    return _valid_arg_size(cmd_str) and _command_exists(cmd_str)

def _valid_arg_size(str):
    # TODO this might need fixing/removing
    """ Is the command 2 or more? """
    return len(str.split()) >= 2

def _command_exists(str):
    """ Is this a command that exists? """
    cmds = ['move', 'turn']
    cmd = str.split()[0]
    return cmd in cmds

