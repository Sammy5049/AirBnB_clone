#!/usr/bin/python3
"""Represent HBnB console."""
import cmd
import re
from shlex import split
from models.place import Place
from models.city import City
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage
from models.user import User


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Represent HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing when empty line is received."""
        pass

    def default(self, arg):
        """Default outcome of cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance and print its id.
        """

        try:
            if not arg:
                raise SyntaxError()
            new_list = arg.split(" ")
            kwargs = {}

            for itr in range(1, len(new_list)):
                k, val = tuple(new_list[itr].split("="))
                if val[0] == '"':
                    val = val.strip('"').replace("_", " ")
                else:
                    try:
                        val = eval(val)
                    except (SyntaxError, NameError):
                        continue
                kwargs[k] = val

            if kwargs == {}:
                obj = eval(new_list[0])()
            else:
                obj = eval(new_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Show string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        Displays all instantiated objects, when no class is mentioned."""
        argl = parse(arg)

        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = []
            for ob in storage.all().values():
                if len(argl) > 0 and argl[0] == ob.__class__.__name__:
                    new_obj.append(ob.__str__())
                elif len(new_obj) == 0:
                    new_obj.append(ob.__str__())
            print(new_obj)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Get the number of instances of a given class."""
        argl = parse(arg)
        count = 0

        for ob in storage.all().values():
            if argl[0] == ob.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id adding or updating
        a given attribute dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argl) == 4:
            ob = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in ob.__class__.__dict__.keys():
                valtype = type(ob.__class__.__dict__[argl[2]])
                ob.__dict__[argl[2]] = valtype(argl[3])
            else:
                ob.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            ob = objdict["{}.{}".format(argl[0], argl[1])]
            for key, value in eval(argl[2]).items():
                if (key in ob.__class__.__dict__.keys() and
                        type(ob.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(ob.__class__.__dict__[key])
                    ob.__dict__[key] = valtype(value)
                else:
                    ob.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
