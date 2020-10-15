from django.shortcuts import render, redirect


def form(request):
    return render(request, "index.html")


def result(request):
    return render(request, "result.html")


def submit(request):
    if request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["location"] = request.POST["location"]
        request.session["language"] = request.POST["language"]
        request.session["comment"] = request.POST["comment"]
        return redirect("/result")
    else:
        return redirect("/")