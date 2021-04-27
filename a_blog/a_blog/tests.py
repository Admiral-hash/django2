from django.contrib.auth import get_user models 
from django.test import TestCase
from django.urls import reverse

from models import post

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user{
            username= 'testuser',
            email= 'testemail.com',
            password= 'secret'
        }
        self.post = Post.objects.create{
            title = 'testtitle',
            body= 'testbody',
            author=self.user
        }
    def test_string_representation(self):
        post = Post(title= 'A simple title')
        self.assertEqual(str(post), post.title)
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','a good title')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}', 'View body')
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'home.html')
    def test_post_detail_views(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get ('/post/180000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, 'a good title')
        self.assertTemplateUsed(response, post_details.html)