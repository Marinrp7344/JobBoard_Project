from django.test import TestCase
from django.contrib.auth.models import User
from jobBoard_app.models import Post, Client

class ModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.post = Post.objects.create(title='Test', body = "Test body", pay_rate ="$300",is_visible = True)
        self.client = Client.objects.create(name='Ricardo', email = "john@email.com",user = self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test')
        self.assertEqual(self.post.body, 'Test body')
        self.assertEqual(self.post.pay_rate, '$300')
        self.assertTrue(self.post.is_visible, True)

    def test_client_creation(self):
        self.assertEqual(self.client.name, 'Ricardo')
        self.assertEqual(self.client.email, 'john@email.com')
        self.assertEqual(self.client.user, self.user)
 
 