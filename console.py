#!/usr/bin/python3
""" console that contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models.file_storage import FileStorage
from models import storage


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
    
    def do_destroy(self, arg):
        """Destroy instance"""
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
                storage = FileStorage()
                storage.reload()
                instance_key = "{}.{}".format(class_name, instance_id)
                
                if instance_key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[instance_key]
                    storage.save()
    
    def do_all(self, arg):
        """Display all instance from json file"""
        storage = FileStorage()
        storage.reload()

        if not arg:
            instance_list = list(storage.all().values())
        
        else:
            class_name = arg
            
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            
            else:
                instance_list = [value for key, value in storage.all().items() if key.startswith(class_name + ".")]

        if not instance_list:
            print("** no instance found **")
        
        else:
            for instance in instance_list:
                print(instance.to_dict())
    
    
    def do_update(self, arg):
        """Update an instance with id and class information"""

        args = arg.split()
        storage = FileStorage()
        storage.reload()

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
                instance_key = "{}.{}".format(class_name, instance_id)
                
                if instance_key not in storage.all():
                    print("** no instance found **")
                
                elif len(args) < 3:
                    print("** attribute name missing **")
                
                elif len(args) < 4:
                    print("** value missing **")
                
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    instance = storage.all()[instance_key]

                    if hasattr(instance, attribute_name):
                        attribute_type = type(getattr(instance, attribute_name))
                        try:
                            casted_value = attribute_type(attribute_value)
                        except ValueError:
                            print("** invalid value type **")
                            return

                        setattr(instance, attribute_name, casted_value)
                        storage.save()
                    else:
                        print("** attribute doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
