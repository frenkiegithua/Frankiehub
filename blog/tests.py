from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from .models import Article


class ArticleModelTests(TestCase):

    def test_new_article_defaults_to_draft(self):
        article = Article.objects.create(
            title='Hello', slug='hello', body='Some text',
        )
        self.assertEqual(article.status, 'draft')

    def test_str_returns_title(self):
        article = Article(title='Hello', slug='hello', body='Some text')
        self.assertEqual(str(article), 'Hello')

    def test_duplicate_slug_is_rejected(self):
        Article.objects.create(title='One', slug='same', body='x')
        with self.assertRaises(IntegrityError):
            Article.objects.create(title='Two', slug='same', body='y')


class ArticleListViewTests(TestCase):

    def setUp(self):
        self.url = reverse('blog:article_list')

    def test_page_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_published_article_is_shown(self):
        Article.objects.create(
            title='Visible post', slug='visible', body='x', status='published',
        )
        response = self.client.get(self.url)
        self.assertContains(response, 'Visible post')

    def test_draft_article_is_hidden(self):
        Article.objects.create(
            title='Secret draft', slug='secret', body='x', status='draft',
        )
        response = self.client.get(self.url)
        self.assertNotContains(response, 'Secret draft')

    def test_newest_article_comes_first(self):
        Article.objects.create(
            title='Older post', slug='older', body='x', status='published',
        )
        Article.objects.create(
            title='Newer post', slug='newer', body='x', status='published',
        )
        response = self.client.get(self.url)
        titles = [a.title for a in response.context['articles']]
        self.assertEqual(titles, ['Newer post', 'Older post'])
