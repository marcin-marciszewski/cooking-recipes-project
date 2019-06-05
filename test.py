import unittest
from project import app


class FlaskTestCase(unittest.TestCase):
    
   
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Add a new recipe' in response.data)
        
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Please login' in response.data)
    
    def test_register(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Please register' in response.data)
        
    def test_get_cuisines(self):
        tester = app.test_client(self)
        response = tester.get('/get_cuisines', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Manage Cuisines' in response.data)
        
    def test_new_cuisines(self):
        tester = app.test_client(self)
        response = tester.get('/new_cuisine', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Add cuisine' in response.data)
        
    def test_get_recipes(self):
        tester = app.test_client(self)
        response = tester.get('/get_recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Recipes' in response.data)
        
    def test_add_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/add_recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Add Recipe' in response.data)
    
    def test_mailto(self):
        tester = app.test_client(self)
        response = tester.get('/mailto', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Send Message' in response.data)
        
    def test_statistics(self):
        tester = app.test_client(self)
        response = tester.get('/statistics', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Total Numeber of Recipes' in response.data)
   
     
    
        
 

if __name__ == '__main__':
    unittest.main()