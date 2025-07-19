import unittest
from functions.get_files_info import get_files_info


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.get_files_info = get_files_info()

    def test_current_dir(self):
        result = self.get_files_info("calculator", ".")
        self.assertEqual(result, 
        "Result for current directory:
        - main.py: file_size=576 bytes, is_dir=False
        - tests.py: file_size=1343 bytes, is_dir=False
        - pkg: file_size=92 bytes, is_dir=True
        - lorem.txt: file_size=28 bytes, is_dir=False")

    def test_pkg_dir(self):
        result = self.get_files_info("calculator", "pkg")
        self.assertEqual(result,
        "Result for 'pkg' directory:
        - calculator.py: file_size=1739 bytes, is_dir=False
        - render.py: file_size=768 bytes, is_dir=False
        - __pycache__: file_size=96 bytes, is_dir=True
        - morelorem.txt: file_size=26 bytes, is_dir=False")
     
    def test_bin_dir(self):
        result = self.get_files_info("calculator", "/bin")
        self.assertEqual(result,
        "Result for '/bin' directory:
        Error: Cannot list "/bin" as it is outside the permitted working directory")
    
    def test_upalevel_dir(self):
        result = self.get_files_info("calculator", "../")
        self.assertEqual(result,
        "Result for '../' directory:
        Error: Cannot list "../" as it is outside the permitted working directory")

if __name__ == "__main__":
    unittest.main()
