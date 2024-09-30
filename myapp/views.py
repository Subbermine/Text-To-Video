from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        print(f"Prompt: {prompt}")
        return redirect("second_page")
    return render(request, "myapp/index.html")


def secondpage(request):
    return render(request, "myapp/second.html")
