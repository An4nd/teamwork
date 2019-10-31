from django.views.generic import TemplateView


class PersonalView(TemplateView):
    template_name = 'personal.html'


class TeamView(TemplateView): # new
    template_name = 'team.html'
