from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PostForm


class IndexView(FormView):
    form_class = PostForm
    template_name = 'form/index.html'


    def form_valid(self, form):
        return render(self.request, 'form/echo.html', {'response': self.request.POST})
