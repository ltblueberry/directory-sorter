import unittest
import os
from directory_sorter import main as script
from directory_sorter import messages


class ScriptTest(unittest.TestCase):

    def test_dir_empty(self):
        exit_message = script(None)
        self.assertEqual(exit_message, messages.NONE_DIR)

    def test_dir_not_found(self):
        directory = "no_directory"
        exit_message = script(directory)
        self.assertEqual(exit_message, messages.DIR_NOT_FOUND.format(
            os.path.abspath(directory)))

    def test_is_not_dir(self):
        not_directory = "testfile"
        exit_message = script(not_directory)
        self.assertEqual(exit_message, messages.IS_NOT_DIR.format(
            os.path.abspath(not_directory)))


if __name__ == '__main__':
    unittest.main()
