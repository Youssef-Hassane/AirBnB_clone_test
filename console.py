#!/usr/bin/python3
"""	HBNB console """
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()

