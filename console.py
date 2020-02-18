#!/usr/bin/python3
"""console for airbnb project"""
import cmd
import shlex
import json


class HBNBCommand(cmd.Cmd):

    """class for command module"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """Create new instance"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        pass

    def do_show(self, args):
        """Print class name and id"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            Print("** instance id missing **")
        pass

    def do_destroy(self, args):
        """Delete class name and id"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        pass

    def do_all(self, args):
        """Print all class name"""
        args = shlex.split(args)
        if args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        pass

    def do_update(self, line):
        """ Updates  """
        pass

    def emptyline(self):
        """print a new empty line"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_EOF(self, line):
        """EOF quit"""
        return True

    def do_quit(self, line):
        """Quit"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
