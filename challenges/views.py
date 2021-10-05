from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenge_obj = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for atleast 20min everyday',
    'march': 'Learn django for atleast 20min everyday',
    'april': 'Take 02 days off from office',
    'may': 'Complete reading a book',
    'june': 'Start to work on a new job',
    'july': 'Spend spare time with friends',
    'august': 'Take improvement courses',
    'september': 'Shift family to a different city',
    'october': 'Bring furniture',
    'november': 'Goto my hometown',
    # 'december': 'Take some leaves from office',
    'december': None,
}


def index(request):
    months = list(monthly_challenge_obj.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenge_obj.keys())

    try:
        redirect_month = months[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

    except:
        # return HttpResponseNotFound("<h3>This month is not supported</h3>")
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenge_obj[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
            "title": 'Monthly challenge'
        })

    except:
        # return HttpResponseNotFound("<h3>This month is not supported</h3>")
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
