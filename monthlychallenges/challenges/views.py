from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
monthlychallenges={"january":"do some workout",
                   "february":"do some ketabells",
                   "march":"spring season has arrived time for some yoga",
                   "april":"do ketabells",
                   "may":"swim for 100 m",
                   "june":"so ja bhai bohot garmi hai",
                   "july":"barish ho rahi hai bahar fotbaal khel",
                   "august":"best mausam to play badminton and loose some pounds",
                   "september":"bhai kuch kar le bhai 9 months ho gaye 1 pound bhi koose nhi kiya",
                   "october":"bhai mubarak ho adha pound loose hua",
                   "november":"bhai tarakki hai ek pound loose ho gaya",
                   "december":None
                   }
# Create your views here.
def monthly_challanges_by_num(request,month):
    months=list(monthlychallenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    redirect_month=months[month-1]
    redirect_path=reverse("monthname",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
def monthly_challanges(request,month):
    try:
        advice=monthlychallenges[month]
        return render(request,"challenges/challenge.html",{
            "text":advice,
            "title":month
        })
    except:
        return HttpResponseNotFound("<h2>This month is not supported try writting the url in the lower case or try writing the correct month</h2>")
    
def func(request):
    months=list(monthlychallenges.keys())
    return render(request,"challenges/base.html",{
        "months":months
    })
 