from logic import rmlogic, RemovalService, UploadService

from unittest import mock
import unittest
import logging



class RmTestCase(unittest.TestCase):
    @mock.patch('logic.os.path')
    @mock.patch('logic.os') #mock object where it is used, not where it came from
    def test_rm(self, mock_os, mock_path):
        # mock setup
        mock_path.isfile.return_value = False

        rmlogic("any path")

        # test that the remove call was not called
        self.assertFalse(mock_os.remove.called, "Failed to not remove if not a file")
        
        # make the file into a file
        mock_path.isfile.return_value = True

        rmlogic("any path") 
        
        # test that rm called os.remove with the rights parameters
        mock_os.remove.assert_called_with("any path")



class RemovalSeriveTestCase(unittest.TestCase):
    # beware if import submodule, magickmock objects return order is not guaranteed
    @mock.patch('logic.os.path')  
    @mock.patch('logic.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate teh service 
        ref = RemovalService()

        # mock setup
        mock_path.isfile.return_value = False
        mock_os.return_value = "Im mockos"
        mock_path.return_value = "Im mockpath"
        logging.info(mock_os())
        logging.info(mock_path())
        
        ref.rm("any path")

        # test that the remove call not called
        self.assertFalse(mock_os.remove.called, "Faileiiid to not remove the file if not a file")

        # turn the file into a file
        mock_path.isfile.return_value = True

        ref.rm("any path")

        mock_os.remove.assert_called_with("any path")


class UploadServiceTestCase(unittest.TestCase):

    # OPTION1 mocking the instance method 'rm' of class RemovalService
    @mock.patch.object(RemovalService, "rm")
    def test_upload_complete(self, mock_rm):
        # build deps
        removal_service = RemovalService()
        ref = UploadService(removal_service)

        #call upload_complete, which calls 'rm'
        ref.upload_complete("up file")

        # check that 'rm' was called on any RemovalService instance
        mock_rm.assert_called_with("up file")

        # check that 'rm' from local RemovalService instance was called
        removal_service.rm.assert_called_with("up file")



class UploadServiceTestCase2(unittest.TestCase):

    # OPTION2 mocking the RemovalService and supply it to UploadService
    def test_upload_complete(self):
        # build deps
        mock_removal_service = mock.create_autospec(RemovalService)
        ref = UploadService(mock_removal_service)

        #call upload_complete, which calls 'rm'
        ref.upload_complete("up file")

        # test that the rm method was called 
        mock_removal_service.rm.assert_called_with("up file")




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()