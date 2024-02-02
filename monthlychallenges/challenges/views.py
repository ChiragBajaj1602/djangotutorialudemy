from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
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
                   "december":"bhai bohot thand hai kya karega weight kam karke"
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
        advice=f'<h1>{monthlychallenges[month]}</h1>'
        return HttpResponse(advice)
    except:
        return HttpResponseNotFound("<h2>This month is not supported try writting the url in the lower case or try writing the correct month</h2>")
    
def func(request):
    listitems=""
    months=list(monthlychallenges.keys())
    for month in months:
        capitalize_month=month.capitalize()
        pathtoredirect=reverse("monthname",args=[month])
        listitems+=f'<li><h1><a href=\"{pathtoredirect}\">{capitalize_month}</a></h1></li>'
        response_data=f"<ul>{listitems}</ul>"
    return HttpResponse(response_data)
 