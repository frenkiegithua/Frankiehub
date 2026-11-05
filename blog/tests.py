from django.db import IntegrityError
from django.test import TestCase

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
