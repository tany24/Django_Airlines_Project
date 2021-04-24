import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','PROJECT_1.settings')

import django
django.setup()

##  FAKE POPULATE SCRIPT
import random
from app2.models import UserInfo
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        # get the topic for the entry

        # create the fake data for that entry
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.free_email()

        # Create the new User entry
        random_user = UserInfo.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,emailID=fake_email)[0]

if __name__ == '__main__':
    print("\n\tPopulating script ! ")
    populate(20)
    print("\n\tPopulating complete ! ")
