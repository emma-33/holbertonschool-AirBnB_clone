import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    def test_instance(self):
        """Test if instance is created"""
        state = State(name="California")
        self.assertIsInstance(state, State)

    def test_attribute_type(self):
        """Test attribute types"""
        state = State(name="California")
        self.assertIsInstance(state.name, str)

    def test_attribute_value(self):
        """Test attribute values"""
        state = State(name="California")
        self.assertEqual(state.name, "California")

    def test_created_at(self):
        """Test created_at attribute"""
        state = State(name="California")
        self.assertIsInstance(state.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        state = State(name="California")
        self.assertIsInstance(state.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict method"""
        state = State(name="California")
        state_dict = state.to_dict()
        expected_keys = ["id", "created_at", "updated_at", "__class__", "name"]
        self.assertCountEqual(state_dict.keys(), expected_keys)

    def test_str_representation(self):
        """Test __str__ method"""
        state = State(name="California")
        str_representation = str(state)
        self.assertIn("[State]", str_representation)
        self.assertIn("'name': 'California'", str_representation)


if __name__ == "__main__":
    unittest.main()
