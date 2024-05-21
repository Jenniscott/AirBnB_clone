#!/usr/bin/python3

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test that all() returns the correct dictionary."""
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

    def test_new(self):
        """Test that new() correctly adds an object to __objects."""
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

    def test_save(self):
        """Test that save() correctly serializes __objects to the JSON file."""
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test that reload() correctly deserializes the JSON file to __objects."""
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

if __name__ == "__main__":
    unittest.main()
