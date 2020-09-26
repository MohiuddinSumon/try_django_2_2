from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ContactForm

company_name = "Daily Code Hour"


# @login_required
def home_page(request):
    return HttpResponse("<h1>Hi</h1>")


def about(request):
    return render(request, "about.html", {"title": "about", "company":company_name})


def contact(request):
    print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "contact page",
        "company": company_name,
        "form": form
    }
    return render(request, "contact.html", context)


def user(request):
    context = {"title": "user page", "company":company_name}
    if request.user.is_authenticated:
        context = {"title": "user page", "company": company_name, "my_list":[1,2,3,4] }

    return render(request, "user.html", context)

