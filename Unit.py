import unittest
import TE3Database

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("John", TE3Database.find_name_by_id(14))  # add assertion here
        self.assertEqual("Bob", TE3Database.find_name_by_id(54))
        self.assertEqual("Something", TE3Database.find_name_by_id(439))



if __name__ == '__main__':
    unittest.main()
