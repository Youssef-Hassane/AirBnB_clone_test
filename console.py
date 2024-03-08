#!/usr/bin/python3
"""	HBNB console """
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Handles End Of File (EOF) character
        """
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id.
            - If the class name is missing,
                print ** class name missing ** (ex: $ create)
            - If the class name doesn’t exist,
                print ** class doesn't exist ** (ex: $ create MyModel)
        """
        if (arg is None) or (arg == ""):
            print("** class name missing **")
            return
        try:
            # Search for and access classes based on <arg>
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        # If the class specified by the string in <arg> does not exist
        # eval(arg) will raise a NameError.
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
