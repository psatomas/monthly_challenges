from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Read a book for at least 20 minutes every day!",
    "may": "Practice coding for at least 20 minutes every day!",
    "june": "Meditate for at least 20 minutes every day!",
    "july": "Drink at least 2 liters of water every day!",
    "august": "Sleep for at least 7 hours every night!",
    "september": "Write a journal entry every day!",
    "october": "Try a new hobby for at least 20 minutes every day!",
    "november": "Practice gratitude by writing down 3 things you're thankful for every day!",
    "december": None
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month < 1 or month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_months = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_months])
    return HttpResponseRedirect(redirect_path)


        

def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenges_text,
            "month_name": month
        })
    except:
        raise Http404()
    