#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel

"""This module contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    # global class_dict
    # class_dict = {"Place": "Place", "State": "State", "City": "City", "Amenity": "Amenity", "Review": "Review"}
    prompt = "(hbnb)"

    def do_create(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
        if len(args) == 1:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
        if arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")

        if len(args) == 1:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
        if len(args) == 1:
            if args[0] == "BaseModel":
                print("** instance id missing **")

        if len(args) == 2:
            dict = models.storage.all()
            # Key has format <className>.id
            key = args[0] + "." + str(args[1])
            if key in dict:
                print(dict[key])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")

        if len(args) == 1:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
        if len(args) == 1:
            if args[0] == "BaseModel":
                print("** instance id missing **")

        if len(args) == 2:
            dict = models.storage.all()
            # Key has format <className>.id
            key = args[0] + "." + str(args[1])
            if key in dict:
                del dict[key]
                models.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):
        dict = models.storage.all()
        args = arg.split()
        if not args:
            for key in dict:
                print(dict[key])
        if len(args) == 1 and args[0] == "BaseModel":
            for key in dict:
                print(dict[key])
        if len(args) == 1 and args[0] != "BaseModel":
            print("** class doesn't exist **")

    def do_update(self, arg):
        dict = models.storage.all()
        args = arg.split()

        if not args:
            print("** class name missing **")
        if len(args) == 1 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        if len(args) == 1 and args[0] == "BaseModel":
            print("** instance id missing **")
        if len(args) == 2:
            key = args[0] + "." + str(args[1])
            if key in dict:
                print("** attribute name missing **")
            else:
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
                print("** no instance found **")

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
