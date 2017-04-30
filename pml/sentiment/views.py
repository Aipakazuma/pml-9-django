from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ReviewForm
from django.utils import timezone


class IndexView(FormView):
    form_class = ReviewForm
    template_name = 'sentiment/index.html'


    def form_valid(self, form):
        return render(self.request, 'sentiment/confirm.html', {'response': self.request.POST})


def registry(request):
    if request.method != 'POST':
        form = ReviewForm()
        return render(request, 'sentiment/index.html', {'form': form})

    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.created = timezone()
        review.save()
        return render(request, 'sentiment/completed.html', {'review': review})
    return render(request, 'sentiment/index.html', {'form': form})
