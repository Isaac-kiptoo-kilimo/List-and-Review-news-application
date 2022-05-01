import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article =Article(1234,'Python Must Be Crazy','A thrilling new Python Series','A thrilling new Python Series','/khsjha27hbs','News', 'analysis from the Middle East' ,8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))