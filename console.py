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
import re
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
            print(arg)
            print(args)
            key = args[0] + "." + str(args[1])
            if key in dict:
                for i in range(2, len(args), 2):
                    attribute = args[i]
                    value = args[i+1]
                    dict[key].__dict__[attribute] = value
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
            line_args = []
            args_1, args_2 = args
            command, args_3 = args_2.split("(")
            args_3 = shlex.split(args_3)
            if len(args_3) == 1:
                args_3 = args_3[0].replace(")", "")
                line = f"{command} {args_1} {args_3}"
                return line

            else:
                line_1 = command
                line_2 = args_1
                line_args.append(line_1)
                line_args.append(line_2)
                item_1 = args_3[1]
                item_2 = "{"
                if item_2 not in item_1:
                    line_args.append(re.sub(r'[,()]', '', args_3[0]))
                    line_args.append(re.sub(r'[,()]', '', args_3[1]))
                    try:
                        line_args.append(re.sub(r'[,()]', '', args_3[2]))
                    except IndexError:
                        pass

                    line = f"{' '.join(line_args)}"
                    return line

                if item_2 in item_1:
                    for i in range(0, len(args_3)):
                        formatted_args = re.sub(r'[{}():,]', '', args_3[i])
                        line_args.append(formatted_args)
                        line = f"{' '.join(line_args)}"
                    return line
        return arg


if __name__ == "__main__":
    HBNBCommand().cmdloop()
