from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from jobBoard_app.models import Post, Client

class PostViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.clients = Client.objects.create(name='Ricardo', email="john@email.com", user=self.user)
        self.client.force_login(self.user)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobBoard_app/index.html')
        
    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        post = Post.objects.create(title='Test', body="Test body", tools="Rake", pay_rate="$300", is_visible=True, client=self.clients)
        response = self.client.get(reverse('post-detail', kwargs={'pk':post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobBoard_app/post_detail.html')

    def test_create_post_view(self):
        formData = {'title': 'New', 'body': "new things", 'tools': 'Rake', 'pay_rate': "$432", 'is_visible': True}
        response = self.client.post(reverse('create-post'), data=formData)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('index'))

    def test_create_post_invalid_view(self):
        response = self.client.post(reverse('create-post'), {})
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'jobBoard_app/post_form.html')

    def test_update_post_view(self):
        post = Post.objects.create(title='Test', body="Test body", tools="Rake", pay_rate="$300", is_visible=True, client=self.clients)
        response = self.client.post(reverse('update-post', kwargs={'post_id':post.id}))
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'jobBoard_app/post_update.html')
    
    def test_delete_post_view(self):
        post = Post.objects.create(title='Test', body="Test body", tools="Rake", pay_rate="$300", is_visible=True, client=self.clients)
        response = self.client.get(reverse('delete-post', kwargs={'post_id':post.id}))
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'jobBoard_app/post_delete.html')
    

    def test_tool_post_view(self):
        post = Post.objects.create(title='Test', body="Test body", tools="Lawn Mower", pay_rate="$300", is_visible=True, client=self.clients)
        response = self.client.post(reverse('display-tools', kwargs={'tool_name':post.tools}))
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'jobBoard_app/display_tools.html')
    
    def test_tool_api_post_view(self):
        post = Post.objects.create(title='Test', body="Test body", tools="Rake", pay_rate="$300", is_visible=True, client=self.clients)
        response = self.client.post(reverse('display-tools-api', kwargs={'tool_name':post.tools}))
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'jobBoard_app/display_tools_api.html')

