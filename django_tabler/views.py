from django.shortcuts import render


def error400(request):
    return render(request, 'django_tabler/400.html', status=400)


def error403(request):
    return render(request, 'django_tabler/403.html', status=403)


def error404(request):
    return render(request, 'django_tabler/404.html', status=404)


def error500(request):
    return render(request, 'django_tabler/500.html', status=500)
