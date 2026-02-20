"""Unit tests for FileManager class."""

import os
import unittest
from file_manager import FileManager


TEST_FILE = "data/test_file.json"
INVALID_FILE = "data/invalid.json"


class TestFileManager(unittest.TestCase):
    """Test cases for FileManager persistence methods."""

    def tearDown(self):
        """Clean test files after each test."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

        if os.path.exists(INVALID_FILE):
            os.remove(INVALID_FILE)

    def test_save_and_load_data(self):
        """Test saving data and loading it correctly."""
        data = [{"id": 1, "name": "Test"}]

        FileManager.save_data(TEST_FILE, data)
        loaded = FileManager.load_data(TEST_FILE)

        self.assertEqual(data, loaded)

    def test_load_nonexistent_file(self):
        """Loading a non-existent file should return empty list."""
        result = FileManager.load_data("data/file_that_does_not_exist.json")
        self.assertEqual(result, [])

    def test_load_invalid_json(self):
        """Loading corrupted JSON should not crash program."""
        with open(INVALID_FILE, "w", encoding="utf-8") as file:
            file.write("{ invalid json")

        result = FileManager.load_data(INVALID_FILE)

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
