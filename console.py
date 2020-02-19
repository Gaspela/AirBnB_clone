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

    all_classes = {"BaseModel", "User", "State", "City",
                       "Amenity", "Place", "Review"}

    def emptyarg(self):
        """Ignor empty spaces"""
        pass

    def do_quit(self, arg):
        """Quit command"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit at end of file"""
        return True

    def help_quit(self):
        """Quit command"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """EOF command to quit"""
        print("EOF command to exit the program\n")

    def do_create(self, arg):
        """Creates a new instance of basemodel"""
        try:
            if not arg:
                raise SyntaxError()
            _list = arg.split(" ")
            obj = eval("{}()".format(_list[0]))
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name mising **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the str of an instance"""
        _line = shlex.split(arg)
        if len(_line) == 0:
            print("** class name missing **")
        elif _line[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(_line) == 1:
            print("** instance id missing **")
        elif len(_line) == 2:
            k = _line[0] + "." + _line[1]
            ob = storage.all()
            if ob.get(k):
                print(ob[k])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance"""
        try:
            if not arg:
                raise SyntaxError()
            _list = arg.split(" ")
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

    def do_all(self, arg):
        """Print all str of all instances"""
        objects = storage.all()
        a_list = []
        if arg:
            if arg in self.all_classes:
                for k, v in objects.items():
                    splitkey = k.split(".")
                    if splitkey[0] == arg:
                        a_list.append(str(v))
            else:
                print("** class doesn't exist **")
        else:
            for v in objects.values():
                a_list.append(str(v))

        print(a_list)

    def do_update(self, arg):
        """Adding or updating attributes"""
        _line = shlex.split(arg)
        if len(_line) == 0:
            print("** class name missing **")
        elif _line[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(_line) == 1:
            print("** instance id missing **")
        elif len(_line) == 2:
            if storage.all().get(_line[0] + "." + _line[1]):
                print("** attribute name missing **")
            else:
                print("** no instance found **")
        elif len(_line) == 3:
            print("** value missing **")
        else:
            if _line[0] in self.all_classes:
                k = _line[0] + "." + _line[1]
                ob = storage.all()
                if k in ob:
                    obj = ob.get(k)
                    try:
                        attr = getattr(obj, _line[2])
                        setattr(obj, _line[2], type(attr)(_line[3]))
                    except:
                        setattr(obj, _line[2], _line[3])
                    storage.save()
                else:
                    print("** no instance found **")


"""Interactive or no interactive mode"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
