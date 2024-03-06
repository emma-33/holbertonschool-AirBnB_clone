#!/usr/bin/python3
""" console that contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models import FileStorage
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Create class HBNB"""
    prompt = "(hbnb) "
    class_name = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

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
                print("** class doesn't exist **")

    def do_show(self, arg):
        """display representation of instance"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        else:
            class_name = args[0]

        if class_name not in globals():
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            instance_id = args[1]
            instance_key = f"{class_name}.{instance_id}"

            if instance_key not in storage.all():
                print("** no instance found **")

            else:
                print(storage.all()[instance_key].to_dict())

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
                instance_list = [
                    value for key, value in storage.all().items()
                    if key.startswith(class_name + ".")]

        if not instance_list:
            print("** no instance found **")

        else:
            for instance in instance_list:
                print(instance.to_dict())


    def do_update(self, arg):
        """Update an instance with id and class information"""
        args = arg.split()

        if not args:
            print("** class name missing **")

        elif args[0] not in self.class_name:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            obj = all_objects.get(key)

            if obj:
                setattr(obj, args[2], eval(args[3]))
                storage.save()

            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
