import unittest
import MySQLdb

class TestMySQLInteraction(unittest.TestCase):

    def setUp(self):
        # Connect to your MySQL database
        self.connection = MySQLdb.connect(
            host='localhost',
            user='root',
            password='@Adeola1234567',
            database='AirBnB_clone_v2'
        )
        self.cursor = self.connection.cursor()

        # Create a table for testing (if not already created)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS states (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """)

        # Clear existing data in the table for a clean test
        self.cursor.execute("DELETE FROM states")
        self.connection.commit()

    def tearDown(self):
        # Clean up after each test by closing database connections
        self.cursor.close()
        self.connection.close()

    def test_add_state(self):
        # Get initial count of records in the table
        initial_count = self.get_record_count()

        # Execute the command to add a new state
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.connection.commit()

        # Get count of records after adding the state
        final_count = self.get_record_count()

        # Assert that the count increased by 1
        self.assertEqual(final_count, initial_count + 1)

    def get_record_count(self):
        # Helper method to get the number of records in the 'states' table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count = self.cursor.fetchone()[0]
        return count

if __name__ == '__main__':
    unittest.main()
