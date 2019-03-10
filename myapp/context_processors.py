from django.conf import settings as sett

def settings(request):
    return sett.__dict__['_wrapped'].__dict__