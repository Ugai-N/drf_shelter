import datetime

from celery import shared_task

from shelter.models import Dog


@shared_task
def SendSetLikeMessage(chat_id):
    print("sent")

@shared_task
def SendBirthdayMail():
    dog_list = Dog.objects.filter(birth=datetime.date.today())
    for dog in dog_list:
        print('dog.name')
