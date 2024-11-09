from django.shortcuts import render, redirect
from .forms import UserFeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback_success.html', {'message': 'Thank you for your feedback!'})
    else:
        form = UserFeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})
