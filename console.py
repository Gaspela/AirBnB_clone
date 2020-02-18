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
from models.place import Place3
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter """
    prompt = "(hbnb) "

    all_classes = {"BaseModel", "User", "State", "City",
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
            obj = eval("{}()".format(_list[0]))
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name mising **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Print the str of an instance"""
        try:
            if not line:
                raise SyntaxError()
            _list = line.split(" ")
            if _list[0] not in self.all_classes:
                raise NameError()
            if len(_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = _list[0] + '.' + _list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance"""
        try:
            if not line:
                raise SyntaxError()
            _list = line.split(" ")
            if len(_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = _list[0] + '.' + _list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Print all str of all instances"""
        objects = storage.all()
        _list = []
        if not line:
            for key in objects:
                _list.append(objects[key])
            print(_list)
            return
        try:
            args = line.split(" ")
            if args[0] not in self.all_classes:
                raise NameError()
            for key in objects:
                name = key.split('.')
                if name[0] == args[0]:
                    _list.append(objects[key])
            print(_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Adding or updating attributes"""
        _list = line.split(" ")
        print(_list)
        objects = storage.all()
        print(objects[_list[0] + "." + _list[1]])
        if len(_list) < 1:
            print("** class name missing** ")
        elif _list[0] in self.all_classes:
            if len(_list) < 2:
                print("** instance id missing **")
            elif _list[0] + "." + _list[1] in objects:
                if len(_list) < 3:
                    print("** attribute name missing **")
                elif len(_list) < 4:
                    print("** value missing **")
                else:
                    instance = objects[_list[0] + "." + _list[1]]
                    setattr(instance, _list[2], _list[3])
                    storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")


"""Interactive or no interactive mode"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
