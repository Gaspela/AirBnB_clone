#!/usr/bin/python3
"""
Program that contain the entry point of the command interpreter
"""

import shlex
import cmd
from datetime import datetime
import models
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter """
    prompt = "(hbnb) "

    classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}

    def emptyline(self):
        """Ignor empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command"""
        return True

    def do_EOF(self, line):
        """Quit command to exit at end of file"""
        return True

    def help_quit(self):
        """Quit command"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """EOF command to quit"""
        print("EOF command to exit the program\n")

    def do_create(self, line):
        """Creates a new instance of basemodel"""
        try:
            if not line:
                raise SyntaxError()
            _list = line.split(" ")
            objectsj = eval("{}()".format(_list[0]))
            objectsj.save()
            print("{}".format(objectsj.id))
        except SyntaxError:
            print("** class name mising **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the str of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if objects.get(key):
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance"""
        try:
            if not line:
                raise SyntaxError()
            _list = line.split(" ")
            if len(_list) < 2:
                raise IndexError()
            objectsjects = storage.all()
            keyey = _list[0] + '.' + _list[1]
            if keyey in objectsjects:
                del objectsjects[keyey]
                storage.save()
            else:
                raise keyeyError()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except keyeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all str of all instances"""
        objects = storage.all()
        _list = []
        if arg:
            if arg in self.classes:
                for key, value in objects.items():
                    splitkeyey = key.split(".")
                    if splitkeyey[0] == arg:
                        _list.append(str(value))
            else:
                print("** class doesn't exist **")
        else:
            for value in objects.values():
                _list.append(str(value))

        print(_list)

    def do_update(self, line):
        """Adding or updating attributes"""
        _list = line.split(" ")
        print(_list)
        objectsjects = storage.all()
        print(objectsjects[_list[0] + "." + _list[1]])
        if len(_list) < 1:
            print("** class name missing** ")
        elif _list[0] in self.classes:
            if len(_list) < 2:
                print("** instance id missing **")
            elif _list[0] + "." + _list[1] in objectsjects:
                if len(_list) < 3:
                    print("** attribute name missing **")
                elif len(_list) < 4:
                    print("** value missing **")
                else:
                    instance = objectsjects[_list[0] + "." + _list[1]]
                    setattr(instance, _list[2], _list[3])
                    storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")


"""Interactive or no interactive mode"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
