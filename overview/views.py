from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeView(View):

    def render(self, request):
        return render(request, 'home_view.html')
    
    def get(self, request):
        return self.render(request)
    


    