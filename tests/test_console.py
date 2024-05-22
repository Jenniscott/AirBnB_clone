#!/usr/bin/python3
from console import HBNBCommand
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
import subprocess
"""Add the parent directory to the sys.path to import console"""
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class ConsoleTests(unittest.TestCase):
    """Unit tests for HBNBCommand class."""

    def setUp(self):
        """Set up test environment."""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(output.getvalue().strip(), '')

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(output.getvalue().strip(), '')

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("")
            self.assertEqual(output.getvalue().strip(), '')

    def test_help(self):
        """Test the help command in interactive mode."""
        result = subprocess.run(["python3", "console.py"],
                                input="help\n",
                                text=True,
                                capture_output=True)
        expected_output = "\nDocumented commands(type help < topic >) -
        \n========================================\nEOF  all  create \
        destroy  help  quit  show  update\n\n"
        self.assertIn(expected_output.strip(), result.stdout.strip())

    def test_non_interactive_mode(self):
        """Test commands in non-interactive mode."""
        commands = 'help\n'
        result = subprocess.run(["python3", "console.py"],
                                input=commands,
                                text=True,
                                capture_output=True)
        expected_output = "(hbnb) \nDocumented commands (type help <topic>):\n========================================\nEOF  all  create  destroy  help  quit  show  update\n\n(hbnb)"
        self.assertIn(expected_output.strip(), result.stdout.strip())


if __name__ == '__main__':
    unittest.main()
