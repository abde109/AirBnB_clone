import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def test_quit_command(self):
        with self.assertRaises(SystemExit):
            self.console.do_quit(None)

    def test_EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.do_EOF(None))
            self.assertEqual(f.getvalue(), '\n')

    def test_emptyline_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.emptyline()
            self.assertEqual(f.getvalue(), '')

    def test_quit_command_exits_the_command_interpreter(self):
        self.console = HBNBCommand()
        with self.assertRaises(SystemExit):
            self.console.do_quit(None)

    def setUp(self):
        self.console = HBNBCommand()

    def test_emptyline_command_does_not_execute_anything(self):
        from unittest.mock import patch
        from io import StringIO
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.emptyline()
            self.assertEqual(f.getvalue(), '')

    def setUp(self):
        self.console = HBNBCommand()

    def test_do_create_handles_missing_class_name(self):
        from unittest.mock import patch
        from io import StringIO
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create('')
            self.assertEqual(f.getvalue(), '** class name missing **\n')

    def test_do_show_handles_missing_class_name(self):
        from unittest.mock import patch
        from io import StringIO
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show('')
            self.assertEqual(f.getvalue(), '** class name missing **\n')


if __name__ == '__main__':
    unittest.main()
