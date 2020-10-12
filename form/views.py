from django.shortcuts import render


def form(request):
    context = {"": ""}

    return render(request, "index.html", context)
