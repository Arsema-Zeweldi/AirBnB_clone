#!/usr/bin/python3
""" Console """


import cmd
import shlex
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Command class """
    prompt = '(hbnb)'
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)

    def do_EOF(self, arg):
        return True

    def help_EOF(self):
        print('EOF command to exit the program')

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print('Quit command to exit the program')

    def emptyline(self):
        return False

    def do_create(self, args):
        if len(args) == 0:
            print('** class name missing **')
            return
        my_data = args.split()

        try:
            model = eval(my_data[0])()
            model.save()
            print(model.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        my_data = shlex.split(arg)
        if len(my_data) == 0:
            print("** class name missing **")
            return
        if my_data[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        if len(my_data) == 1:
            print("** instance id missing **")
        storage.reload()
        my_dict = storage.all()
        key = my_data[0] + "." + my_data[1]
        if key in my_dict:
            my_instance = str(my_dict[key])
            print(my_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        my_data = shlex.split(arg)

        if len(my_data) == 0:
            print("** class name missing **")
            return
        if my_data[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return
        if len(my_data) == 1:
            print("** instance id missing **")
            return
        storage.reload()
        my_dict = storage.all()
        key = my_data[0] + "." + my_data[1]
        if key in my_dict:
            del my_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        storage.reload()
        my_json = []
        my_dict = storage.all()
        if not arg:
            for key in my_dict:
                my_json.append(str(my_dict[key]))
            print(json.dumps(my_json))
            return
        my_data = shlex.split(arg)
        if my_data[0] in HBNBCommand.classes.keys():
            for key in my_dict:
                if my_data[0] in key:
                    my_json.append(str(my_dict[key]))
            print(json.dumps(my_json))
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        if not args:
            print("** class name missing **")
            return

        token = args.split()

        if token[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == token[0] and ob_id == token[1].strip('"'):
                    if len(token) == 2:
                        print("** attribute name missing **")
                    elif len(token) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, token[2], token[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
