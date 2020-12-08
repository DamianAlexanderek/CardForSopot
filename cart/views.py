from django.shortcuts import render
from .forms import EmailPostForm


def text_share(request):

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, 'share.html', {'form': form})
