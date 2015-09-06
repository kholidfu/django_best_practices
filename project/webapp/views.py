# core django imports
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class IndexView(View):

    template_name = 'index.html'

    def get(self, request):
        """Regular get method.
        """
        return render(request, self.template_name, {'name': 'django!'})
