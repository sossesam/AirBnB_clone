#!/usr/bin/python3


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        """ type quit to exit console"""
        return True






if __name__ == '__main__':
    HBNBCommand().cmdloop()
