from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from accounts.models import Profile
from game.models import Game
from news.models import News, GameRequest

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()[:5]
        context['games'] = Game.objects.all()[:5]
        context['news'] = News.objects.order_by('time')[:5]
        return context

class GameRequestView(CreateView):
    model = GameRequest
    fields = ('name',)
    template_name = 'gamerequest.html'
