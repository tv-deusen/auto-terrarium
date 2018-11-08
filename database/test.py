import unittest

from .ReadingsDB import ReadingsDB

# ReadingsDB Requirements:
# - Initialization
# - Deletion (or at least freeing space)
# - Multiprocess connection (need to figure how)
# - Insertion
# - Reading

class TestReadingsDB(unittest.TestCase):

    def test_good_init(self):
        db_path = "test.db"
        db = ReadingsDB(db_path)
        self.assertIsNotNone(db, "Failed to initialize database")



