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
    
    def do_show(self, arg):
        """display representation of instance"""
        args = arg.split()
        
        if not args:
            print("** class name missing **")
        
        else:
            class_name = args[0]
        
        if class_name not in globals():
            print("** class doesn't exist **")
        
        elif len(args) < 2:
            print("** instance id missing **")
        
        else:
            instance_id = args[1]
            instance_key = f"{class_name}.{instance_id}"
            
            if instance_key not in BaseModel.instances:
                print("** no instance found **")
            
            else:
                print(BaseModel.instances[instance_key].to_dict())

if __name__ == "__main__":
    HBNBCommand().cmdloop()
