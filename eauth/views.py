from django.http import JsonResponse
from django.shortcuts import render

from crispy_forms.utils import render_crispy_form

from .forms import UserCreationForm

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            return JsonResponse({'success': True})

        # RequestContext ensures CSRF token is placed in newly rendered form_html
        form_html = render_crispy_form(form)
        return JsonResponse({'success': False, 'form_html': form_html})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'success': True})

        form_html = render_crispy_form(form)
        return JsonResponse({'success': False, 'form_html': form_html}) 