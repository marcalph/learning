from logic import rm

import os.path
import tempfile
import unittest

class RmTestCase(unittest.TestCase):
    tmpfilepath = os.patgh.join(tempfile.gettempdir(), "tmptestfile")

    def setUp(self) -> None:
        with open(self.tmpfilepath, "wb") as f:
            f.write("Delete this message!")
    
    def test_rm(self):
        # remoce the file
        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath)), "Failed to remove the file"
