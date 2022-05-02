import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article =Article('abc','mashirima kapombe','Python Must Be Crazy','https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8dmlld3xlbnwwfHwwfHw%3D&w=1000&q=80','A thrilling new Python Series','https://newsapi.org/v2/top-headlines/sources',8-5-2015, 'analysis from the Middle East' ,)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

#     def test_init(self):
#         self.assertEqual(self.new_article.source,'abc')
#         self.assertEqual(self.new_article.author,'mashirima kapombe')
#         self.assertEqual(self.new_article.title,'Python Must Be Crazy')
#         self.assertEqual(self.new_article.image_url,'https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8dmlld3xlbnwwfHwwfHw%3D&w=1000&q=80')
#         self.assertEqual(self.new_article.description_,'Python Must Be Crazy')
#         self.assertEqual(self.new_article.url_,'https://newsapi.org/v2/top-headlines/sources')
#         self.assertEqual(self.new_article.published_at ,8-5-2015)
#         self.assertEqual(self.new_article.content,'analysis from the Middle East')

# if __name__=='__main__':
#     unittest.main()

