#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import shlex

"""This module contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    global class_dict
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
    }
    prompt = "(hbnb)"

    def do_create(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
        if len(args) == 1:
            for key, value in class_dict.items():
                if args[0] == key:
                    new_instance = value()
                    new_instance.save()
                    print(new_instance.id)
                    return
            print("** class doesn't exist **")

    def do_show(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")

        if len(args) == 1:
            for key, value in class_dict.items():
                if key == args[0]:
                    print("** instance id missing **")
                    return
            print("** class doesn't exist **")

        if len(args) == 2:
            dict = models.storage.all()
            key = args[0] + "." + str(args[1])
            if key in dict:
                print(dict[key])
            else:
                for key, value in class_dict.items():
                    if key == args[0]:
                        print("** no instance found **")
                        return
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")

        if len(args) == 1:
            for key, value in class_dict.items():
                if key == args[0]:
                    print("** instance id missing **")
                    return
            print("** class doesn't exist **")

        if len(args) == 2:
            dict = models.storage.all()
            key = args[0] + "." + str(args[1])
            if key in dict:
                del dict[key]
                models.storage.save()
            else:
                for key, value in class_dict.items():
                    if key == args[0]:
                        print("** no instance found **")
                        return
                print("** class doesn't exist **")

    def do_all(self, arg):
        dict = models.storage.all()
        if not arg:
            for key, value in dict.items():
                print(value)

        if arg:
            for key, value in class_dict.items():
                if key == arg:
                    for key, value in dict.items():
                        if key.split(".")[0] == arg:
                            print(value)
                    return
            print("** class doesn't exist **")

    def do_count(self, arg):
        dict = models.storage.all()
        count = 0
        if arg:
            for key, value in class_dict.items():
                if key == arg:
                    for key, value in dict.items():
                        if key.split(".")[0] == arg:
                            count = count + 1
                    print(count)
                    return
            print("** class doesn't exist **")

    # def do_all(self, arg):
    #     print(arg)

    #     dict = models.storage.all()
    #     args = arg.split()
    #     if not args:
    #         for key in dict:
    #             print(dict[key])
    #     if len(args) == 1:
    #         for key, value in class_dict.items():
    #                 if key == args[0]:
    #                     for key in dict:
    #                         print(dict[key])
    #                     return
    #         print("** class doesn't exist **")

    def do_update(self, arg):
        dict = models.storage.all()
        args = arg.split()

        if not args:
            print("** class name missing **")

        if len(args) == 1:
            for key, value in class_dict.items():
                if key == args[0]:
                    print("** instance id missing **")
                    return
            print("** class doesn't exist **")

        if len(args) == 2:
            key = args[0] + "." + str(args[1])
            if key in dict:
                print("** attribute name missing **")
                return
            for key, value in class_dict.items():
                if key == args[0]:
                    print("** instance id missing **")
                    return
            print("** no instance found **")

        if len(args) == 3:
            key = args[0] + "." + str(args[1])
            if key in dict:
                print("** value missing **")
            else:
                print("** no instance found **")
        if len(args) >= 4:
            key = args[0] + "." + str(args[1])
            if key in dict:
                dict[key].__dict__[args[2]] = args[3].strip('"')
                models.storage.save()
            else:
                for key, value in class_dict.items():
                    if key == args[0]:
                        print("** no instance found **")
                        return
                print("** class doesn't exist **")

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_help(self, arg):
        """Help command to display help"""
        cmd.Cmd.do_help(self, arg)

    def precmd(self, arg):
        args = arg.split(".")
        if len(args) == 2:
            args_1 = args[0]
            args_2 = args[1].split("(")
            args_3 = shlex.split(args_2[1].split(")")[0])

            line_1 = args_2[0]
            line_2 = args_1
            try:
                line_3 = args_3[0].split(",")[0]
                line_4 = args_3[1].split(",")[0]
                line_5 = args_3[2]
            except IndexError:
                try:
                    line = f"{line_1} {line_2} {line_3}"
                except:
                     line = f"{line_1} {line_2}"
                     return line
            line = f"{line_1} {line_2} {line_3} {line_4} {line_5}"
            return line

        else:
            return arg


if __name__ == "__main__":
    HBNBCommand().cmdloop()
