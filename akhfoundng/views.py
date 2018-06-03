
from django.shortcuts import render
from django.conf import settings
from  django.http import HttpResponseRedirect

from django.shortcuts import render
from django.template import loader
from django.template.loader import get_template

DEFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.akhorsfallfoundation.org")


# Create your views here.
def wildcard_redirect(request, path=None):
    new_url = DEFAULT_REDIRECT_URL

    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + "/" + path

    return HttpResponseRedirect(new_url)


def home(request):
    return render(request, 'serves/home.html')


def about_us(request):
    return render(request, 'serves/about_us.html')


def our_mission(request):
    return render(request, 'serves/our_mission.html'),


def healthcare(request):
    return render(request, 'serves/healthcare.html')


def youths_empowerment(request):
    return render(request, 'serves/youths_empowerment.html')


def peace_and_security(request):
    return render(request, 'serves/peace_and_security.html')


def education_and_training(request):
    return render(request, 'serves/education_and_training.html')


def donate(request):
    return render(request, 'serves/donate.html')


def vision(request):
    return render(request, 'serves/vision.html')