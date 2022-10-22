from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
from django.contrib.auth.models import User

# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_kim = user.objects.create_user(username="kim", password="somepassword")
        self.user_lee = user.objects.create_user(username="lee", password="somepassword")

    def test_post_list(self):
        response = self.client.get('/blog/', follow=True) #301
        #response 결과가 정상적으로 보이는지
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')

        # title이 정상적으로 보이는지
        self.assertEqual(soup.title.text, 'Blog')

        # navbar이 정상적으로 보이는지
        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About_me', navbar.text)

        # post가 정상적으로 보이는지
        # 1. 맨 처음엔 Post가 없음
        self.assertEqual(Post.objects.count(), 0)
        main_area = soup.find('div', id="main-area")
        self.assertIn('아직 게시물이 없습니다.', main_area.text)

        # 2. Post가 추가
        post_001 = Post.objects.create(title="첫 번째 포스트", content="첫 번째 포스트입니다.",
                                       author=self.user_kim)
        post_002 = Post.objects.create(title="두 번째 포스트", content="두 번째 포스트입니다.",
                                       author=self.user_lee)
        self.assertEqual(Post.objects.count(), 2)

        response = self.client.get('/blog/', follow=True)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        main_area = soup.find('div', id="main-area")
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)

        self.assertIn(post_001.author.username.upper(), main_area.text)
        self.assertIn(post_002.author.username.upper(), main_area.text)

        def test_post_detail(self):
            post_001 = Post.objects.create(title="첫 번째 포스트", content="첫 번째 포스트입니다.",
                                           author=self.user_kim)
            self.assertEqual(post_001.get_absolute_url(), '/blog/1/')

            response = self.client.get(post_001.get_absolute_url(), follow=True)  #'/blog/1/'
            self.assertEqual(response.status_code, 200)
            soup = BeautifulSoup(response.content, 'html.parser')

            # navbar이 정상적으로 보이는지
            navbar = soup.nav
            self.assertIn('Blog', navbar.text)
            self.assertIn('About_me', navbar.text)

            self.assertIn(post_001.title, soup.title.text)

            main_area = soup.find('div', id='main-area')
            post_area = main_area('div', id='post-area')
            self.assertIn(post_001.title, post_area.text)
            self.assertIn(post_001.content, post_area.text)
            self.assertIn(post_001.author.username.upper(), post_area.text)