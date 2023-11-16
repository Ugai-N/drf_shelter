from django.core.management import BaseCommand

from shelter.services import MyBot


class Command(BaseCommand):
    def handle(self, *args, **options):
        my_bot = MyBot()
        my_bot.send_tg_message('hi from Django_DRF_Shelter')
