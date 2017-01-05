from populate import base
import random

from django.contrib.auth.models import User
from article.models import Article, Comment



def populate():
    print('Populating Article and Comment...', end='')
    titles = ['飾品保養＆小常識']
    comments = ['中肯', '太實用了', '完美']
    Article.objects.all().delete()
    Comment.objects.all().delete()
    user = User.objects.first()
    for title in titles:
        article = Article()
        article.title = title
        for j in range(20):
            article.content += title + '\n'
        article.like=random.randint(0,20)
        article.save()
        for comment in comments:
            Comment.objects.create(article=article, content=comment, user=user)
    print('done')
if __name__ == '__main__':
    populate()
    