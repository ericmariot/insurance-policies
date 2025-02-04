from django.http.response import HttpResponse


def healthz(request):
    return HttpResponse()
