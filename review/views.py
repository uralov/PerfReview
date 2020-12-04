from django.shortcuts import render
from django.views.generic import ListView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory

from .models import Review, Answer


class ReviewListView(ListView):
    model = Review
    template_name = 'index.html'


class AnswerInline(InlineFormSetFactory):
    model = Answer
    fields = ['criteria', 'score', 'comment']


class CreateReviewView(CreateWithInlinesView):
    model = Review
    inlines = [AnswerInline]
    fields = ['reviewee', 'date']
    template_name = 'review.html'


class UpdateReviewView(UpdateWithInlinesView):
    model = Review
    inlines = [AnswerInline]
    fields = ['reviewee', 'date']
    template_name = 'review.html'
