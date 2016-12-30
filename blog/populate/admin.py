from populate import base
from django.contrib.auth.models import User
from account.models import UserProfile

def populate():
    print('Creating admin account...', end='')
    User.objects.all().delete()
    admin=User.objects.create_superuser(username='admin', password='admin', email=None)
    User.objects.create(username='admin',fullName='管理者',website='',address='')
    print('done')
if __name__ == '__main__':
    populate()