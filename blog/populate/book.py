from populate import base
import datetime
import random

from book.models import Book


def populate():
    print('Populating books...', end='')
    titles = ['穿在身上的 --草地恐龍時代毛衣','穿在身上的 --星空刺繡暴龍長袖T恤',
              '穿在身上的 --手繪躲貓貓長袖T恤','穿在身上的 --刺繡小鹿坑條毛衣',
              '穿在腿上的 --前口袋棉麻寬褲 ( 灰綠色 / 深灰色 )',
              '穿在腿上的 --刺繡扣復古高腰七分裙 ( 灰 / 藍 )',
              '其他其他的小東西 --窗台上的祕密戒指','其他其他的小東西 --解不開結的戒指',
              '其他其他的小東西 --窗台的祕密戒指','其他其他的小東西 --諾亞之心戒指',
              '裝錢的錢包 --水松木長夾( 彩色 / 原色 )',
              '裝錢的錢包 --手染掛頸手機零錢收納包 ( 海洋 / 夕陽 / 沙漠 )',]
    materials = ['棉麻', 'Cotton, Polyester', 'Portuguese Cork','銀']
    
    Book.objects.all().delete()
    for title in titles:
        book = Book()
        book.title = title
        n = random.randint(0,len(materials)-1)
        book.material=materials[n]
        book.pubdate=datetime.datetime.today()
        book.price=690
        book.save()
    print('done')
if __name__ == '__main__':
    populate()
    