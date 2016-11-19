import unittest
import passpass

class PassPassTestCase(unittest.TestCase):
    def setUp(self):
        self.app = passpass.app.test_client()
    
    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200) 

if __name__ == '__main__':
    unittest.main()