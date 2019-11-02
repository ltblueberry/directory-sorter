import unittest
from os import path, listdir
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
            path.abspath(directory)))

    def test_is_not_dir(self):
        not_directory = "testfile"
        exit_message = script(not_directory)
        self.assertEqual(exit_message, messages.IS_NOT_DIR.format(
            path.abspath(not_directory)))

    def test_sorting(self):
        directory = "test"
        exit_message = script(directory)
        if exit_message != messages.DONE:
            print "Script finished with unexpected message"
            self.assertTrue(False)
            return

        files = [f for f in listdir(
            directory) if path.isfile(path.join(directory, f))]

        # check there are no files in directory
        if files:
            print "There are unmoved files after script finished"
            self.assertTrue(False)
            return

        sub_directories = {"no_extension": 1, "png": 1, "txt": 2}
        for key in sub_directories:
            moved_files = listdir(path.join(directory, key))
            if len(moved_files) != sub_directories[key]:
                print "{} directory has unexpected files count ({} != {})".format(
                    key, len(moved_files), sub_directories[key])
                self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
