#!/usr/bin/python3
""" Unittests for State model."""


from tests.test_models.test_base_model import test_basemodel
from models.state import State

class test_state(test_basemodel):
    """ Test State model functionalities."""
    
    def __init__(self, *args, **kwargs):
        """Initialize the attributes of the newly created object with specified."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test the behavior of the `name3` method."""
        new = self.value()
        self.assertEqual(type(new.name), str)
