from django.test import TestCase

# Create your tests here.
from account.models import User
from article.models import Article


class TestApi(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='mage12138', password="12345678")
        for i in range(0, 100):
            Article.objects.create(content="Test case:"+str(i), user=self.user)
        self.articlecount = Article.objects.all().count()

    def test_article_create(self):
        article = Article.objects.create(content='Created article', user=self.user)
        self.assertEqual(self.articlecount + 1, article.id)
