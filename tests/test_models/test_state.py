#!/usr/bin/python3
""" Unittests for State model."""

from tests.test_models.test_base_model import test_basemodel
from models.state import State
import mysql.connector

class test_state(test_basemodel):
    """ Test State model functionalities."""
    def setUp(self):
        # Connect to the test database
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Adeola1234567',
            database='AirBnB_clone_v2'
        )
        self.cursor = self.conn.cursor()

    def __init__(self, *args, **kwargs):
        """Initialize the attributes of the newly created object with specified """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


    # Clean up any existing test data in the 'states' table (optional)
        self.cursor.execute("DELETE FROM states")
        self.connection.commit()

    def tearDown(self):
        """
        Clean up resources after each test case.
        """
        # Close the cursor and the database connection
        self.cursor.close()
        self.connection.close()

    def test_create_state(self):
        """
        Test creating a new State record in the database.
        """
        # Get the initial count of records in the 'states' table
        initial_count = self._get_record_count()

        # Execute the command to create a new State record ('California')
        state_name = "California"
        new_state = State()
        new_state.name = state_name
        new_state.save()  # Assuming 'save()' method inserts the record into the database

        # Get the count of records after the insert operation
        final_count = self._get_record_count()

        # Check if the difference is +1
        self.assertEqual(final_count, initial_count + 1, "Failed to add a new State record")

    def _get_record_count(self):
        """
        Helper function to get the count of records in the 'states' table.
        """
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count = self.cursor.fetchone()[0]
        return count

if __name__ == '__main__':
    unittest.main()
