from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        # return true or false depending on the conditionals
        "newyear": now.month == 1 and now.day == 1
    })