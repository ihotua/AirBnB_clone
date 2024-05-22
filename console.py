#!/usr/bin/python3
"""This script defines the hbnb console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This defines the command interpreter"""
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return (True)

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return (True)

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_help(self, arg):
        """Help command to list available commands."""
        super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
