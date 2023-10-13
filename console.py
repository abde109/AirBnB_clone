#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBC class for the command interpreter.
    """

    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
