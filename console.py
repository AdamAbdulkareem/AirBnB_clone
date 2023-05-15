#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
"""This module contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hbnb)"

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        new_instance = BaseModel()
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
