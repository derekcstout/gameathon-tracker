from django.shortcuts import render
from django.views.generic import CreateView
from .models import Award


#def awardpoints(request):
    #return render(request, "awards/awardpoints.html")

class AddPointsView(CreateView):
    model = Award
    template_name = 'awards/awardpoints.html'
    fields = '__all__'

