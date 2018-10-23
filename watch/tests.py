from django.test import TestCase
from .models import Comment, Business
# Create your tests here.
class CommentTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.comment = Comment(name='lovely')
    '''
    test instance of comment
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))
        '''
        test for save instance of comment
        '''
    def test_save_comment(self):
        self.comment.save_comment()
        name = Comment.objects.all()
        self.assertTrue(len(name)>0)