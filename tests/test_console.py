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


if __name__ == '__main__':
    unittest.main()
