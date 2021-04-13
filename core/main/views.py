from django.shortcuts import render
from .models import Team, Gallery, Feedback
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import FeedBackForm


def home(request):
    return render(request, 'main/index.html')


class TeamViews(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'main/teams.html', {'teams_list': teams})


def teams_details(request, slug):
    team = Team.objects.get(slug__iexact=slug)
    return render(request, 'main/teams_detail.html', context={'team': team})


class GalleryViews(View):
    def get(self, request):
        gallery = Gallery.objects.all()
        return render(request, 'main/gallery.html', {'gallery_list': gallery})


def feedback(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            response = form.cleaned_data['response']
            data = Feedback(firstname=firstname, lastname=lastname, email=email, message=message, response=response)
            data.save()
            return HttpResponseRedirect('/')
    else:
        form = FeedBackForm()
        return render(request, 'main/feedback.html', {'form': form})
