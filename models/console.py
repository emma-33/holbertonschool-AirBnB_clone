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

    def do_create(self, arg):
        """Create a new instance"""
        if not arg:
            print("** class missing **")
        
        else:
            try:
                class_instance = globals()[arg]()
                class_instance.save()
                print(class_instance.id)
            
            except KeyError:
                print("** class doesn't exist")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
