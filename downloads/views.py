from django.shortcuts import render
from . models import Download

# Create your views here.
def download(request):
    files = Download.objects.all().order_by("-uploaded_at")
    context = {'files':files}
    return render(request, 'core/download.html', context)