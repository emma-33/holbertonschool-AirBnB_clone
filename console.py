#!/usr/bin/python3
""" console that contains the entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """Create class HBNB"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit program"""
        print("quit")
        return (True)
    
    def do_EOF(self, arg):
        """Exit program"""
        print("quit")
        return (True)
    
    def emptyline(self):
        """Nothing emptyline"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
