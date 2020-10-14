from django.shortcuts import render, redirect


def form(request):
    return render(request, "index.html")


def result(request):
    if request.method == "POST":
        context = {
            "name": request.POST["name"],
            "location": request.POST["location"],
            "language": request.POST["language"],
            "comment": request.POST["comment"],
        }
        return render(request, "result.html", context)
    else:
        return redirect("/")