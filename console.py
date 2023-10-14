#!/usr/bin/python3
""" cli using cmd.Cmd module"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from json import dumps


class HBNBCommand(cmd.Cmd):
    """
    HBNBC class for the command interpreter.
    """

    prompt = '(hbnb) '
    models = {'BaseModel': BaseModel, 'User': User}

    def do_quit(self, args):
        """Quits the command interpreter."""
        raise SystemExit

    def do_EOF(self, args):
        """Exit the command interpreter with Ctrl-D."""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn't execute anything."""
        pass

    def do_help(self, args):
        """
        List available commands with "help" or detailed help with "help cmd".
        """
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """creates instance of chosen class,
        saves it to json and prints the id"""

        if not (args):
            print("** class name missing **")
            return
        if (args in self.models.keys()):
            instance = eval(args)()
            instance.save()
            print(instance.id)
            return
        print("** class doesn't exist **")

    def do_show(self, args):
        """shows instance of base based on id"""

        instances = FileStorage()
        instances.reload()
        if (len(args) == 0):
            print("** class name missing **")
            return
        tofind = args.split(' ')
        if (tofind[0] not in self.models):
            print("** class doesn't exist **")
            return
        if (len(tofind) == 1):
            print("** instance id missing **")
            return
        for identifier in list(instances.all()):
            id = identifier.split('.')
            if (id[0] == tofind[0] and id[1] == tofind[1]):

                print(eval(id[0])(**instances.all()[identifier]))
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """remove instance of model based on id"""
        instances = FileStorage()
        instances.reload()
        if (len(args) == 0):
            print("** class name missing **")
            return
        tofind = args.split(' ')
        if (tofind[0] not in self.models.keys()):
            print("** class doesn't exist **")
            return
        if (len(tofind) == 1):
            print("** instance id missing **")
            return
        for identifier in list(instances.all()):
            id = identifier.split('.')
            if (id[0] == tofind[0] and id[1] == tofind[1]):
                instances.all().pop(identifier)
                instances.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """shows all instances with or without model specifier"""

        instances = FileStorage()
        instances.reload()
        result = []
        if (len(args) == 0):
            for identifier in list(instances.all()):
                splitID = identifier.split('.')
                if (splitID[0] in self.models.keys()):
                    result.append(
                        str(eval(splitID[0])(**instances.all()[identifier])))

        else:
            tofind = args.split(' ')
            if (tofind[0] not in self.models):
                print("** class doesn't exist **")
                return

            for identifier in list(instances.all()):
                id = identifier.split('.')
                if (id[0] == tofind[0]):
                    result.append(
                        str(instances.all()[identifier])
)
        print(result)

    def do_update(self, args):
        """update instance attribute of model based on id"""
        instances = FileStorage()
        instances.reload()
        if (len(args) == 0):
            print("** class name missing **")
            return
        tofind = args.split(' ')
        if (tofind[0] not in self.models):
            print("** class doesn't exist **")
            return
        if (len(tofind) == 1):
            print("** instance id missing **")
            return
        if (len(tofind) == 2):
            print("** attribute name missing **")
            return
        if (len(tofind) == 3):
            print("** value missing **")
            return
        for identifier in list(instances.all()):
            id = identifier.split('.')
            value = tofind[3]
            if (id[0] == tofind[0] and id[1] == tofind[1]):
                if value.startswith('"') and value.endswith('"'):
                    instances.all()[identifier][tofind[2]] = eval(
                        tofind[3])
                    print("is string")
                else:
                    try:
                        instances.all()[identifier][tofind[2]] = int(value)
                        print("is int")
                    except ValueError:
                        try:
                            instances.all()[identifier][tofind[2]] = float(
                                value)
                            print("is float")
                        except ValueError:
                            instances.all()[identifier][tofind[2]] = value
                instances.save()
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
