from rest_framework import serializers

SCAM_WORDS = ['крипта', 'биржа', 'продам']


def validator_scam_words(value): # через функцию для использования в сериализаторе
    if set(value.lower().split()) & set(SCAM_WORDS): # чтобы исключить скам слова в названии собаки - взяли множество всех слов в кличке, взяли множество всех скам слов и сделали джоин. вот если в джоине будет не пусто - то вызываем исключение
        raise serializers.ValidationError('SCAM_WORDS!!!')
