#!/usr/bin/python3
import cmd
"""This module contains the entry point of the command interpreter"""

class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hbnb)"
    
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