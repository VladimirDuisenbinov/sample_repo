from .models import URLShort


class URLShortRepo():
    @staticmethod
    def list():
        return URLShort.objects.filter(archived=False)

    @staticmethod
    def retrieve(fields):
        return URLShortRepo.list().filter(**fields).first()

    @staticmethod
    def create(fields):
        return URLShort.objects.create(**fields)
