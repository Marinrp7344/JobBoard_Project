from django.test import TestCase
from jobBoard_app.forms import PostForm,ClientForm
from django.contrib.auth.models import User

class FormTest(TestCase):
    def test_post_form(self):
        formData = {
            'title' : 'Test',
            'body' : 'Test body',
            'description' : 'Test',
            'pay_rate' : '$300',
            'is_visible' : True,
        }
        form = PostForm(data=formData)
        self.assertTrue(form.is_valid())

    def test_client_form(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        formData = {
            'name' : 'Test',
            'email' : 'Test body',
            'user' : self.user,
        }
        form = ClientForm(data=formData)
        self.assertTrue(form.is_valid())
