#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    HBNBC class for the command interpreter.
    """

    prompt = '(hbnb) '
    models = {'BaseModel'}

    def do_quit(self, args):
        """Quits the command interpreter."""
        raise SystemExit

    def do_EOF(self, args):
        """Exit the command interpreter with Ctrl-D."""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
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
        if (args == 'BaseModel'):
            instance = eval(args)()
            instance.save()
            print(instance.id)
            return
        print("** class doesn't exist **")

    def do_show(self, args):

        instances = FileStorage()
        instances.reload()
        """shows instance of base based on id"""
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
                print(instances._objects[identifier])
                return
            print("** no instance found *")

    def do_destroy(self, args):
        instances = FileStorage()
        instances.reload()
        """remove instance of base based on id"""
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
                instances._objects.pop(identifier)
                instances.save()
                return
            print("** no instance found *")

    def do_all(self, args):
        """shows all instances with or without model specifier"""

        instances = FileStorage()
        instances.reload()
        if (len(args) == 0):
            for identifier in list(instances.all()):
                print(instances._objects[identifier])

        else:
            tofind = args.split(' ')
            if (tofind[0] not in self.models):
                print("** class doesn't exist **")
                return

            for identifier in list(instances.all()):
                id = identifier.split('.')
                if (id[0] == tofind[0]):
                    print(instances._objects[identifier])

    def do_update(self, args):
        instances = FileStorage()
        instances.reload()
        """update instance attribute of model based on id"""
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
            if (id[0] == tofind[0] and id[1] == tofind[1]):
                instances._objects[identifier][tofind[2]] = tofind[3]
                instances.save()
                return
            print("** no instance found *")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
