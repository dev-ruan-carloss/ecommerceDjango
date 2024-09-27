from django.shortcuts import render
from django.views import View 


# Create your views here.
def home_view(request):
    return render(request, 'outros_templates/logincadastro.html')

class CadastroView(View):
     def get(self, request):
        return render(request, 'outros_templates/logincadastro.html')