from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ReviewForm
from django.utils import timezone
from .vectorizer import vect
import numpy as np
import os
import pickle

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir,
                 'pkl_objects',
                 'classifier.pkl'), 'rb'))
label = {0: 'negative', 1: 'positive'}


def classify(document):
    X = vect.transform([document])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    return label[y], proba


def train(document, y):
    X = vect.transform([document])
    clf.partial_fit(X, [y])


class IndexView(FormView):
    form_class = ReviewForm
    template_name = 'sentiment/index.html'


    def form_valid(self, form):
        # predictionの実行
        y, proba = classify(self.request.POST['review_text'])
        return render(self.request,
                    'sentiment/confirm.html',
                    {
                        'response': self.request.POST,
                        'prediction': y,
                        'probability': proba
                    })


def registry(request):
    if request.method != 'POST':
        form = ReviewForm()
        return render(request, 'sentiment/index.html', {'form': form})

    feedback = request.POST['feedback_button']
    prediction = request.POST['prediction']
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        y = {v: k for k, v in label.items()}[prediction]
        if feedback == 'Incorrect':
            y = int(not(y))
        train(review.review_text, y)
        review.sentiment = y
        review.created = timezone.now()
        review.save()
        return render(request, 'sentiment/completed.html', {'review': review})
    return render(request, 'sentiment/index.html', {'form': form})
