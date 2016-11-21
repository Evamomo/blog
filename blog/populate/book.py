from populate import base
import datetime
import random
from book.models import Book

def populate():
    print('Populating books...', end='')
    titles = ['我要心動一輩子', '10 分鐘內學好 Python', '簡單學習 Django',
              '連環泡有酒酒', '模仿遊戲', '親親小媽',
              '我要心動一輩子3', '茶花女', '簡單學習 Django3',
              '人生何不迷路一次']
    authors = ['賴佩霞', '張三', '李四','迷路']
    
    Book.objects.all().delete()
    for title in titles:
        book = Book()
        book.title = title
        n = random.randint(0,len(authors)-1)
        book.author=authors[n]
        book.publisher=book.author
        book.pubdate=datetime.datetime.today()
        book.version='1'
        book.price=1000
        book.save()
    print('done')
if __name__ == '__main__':
    populate()
    