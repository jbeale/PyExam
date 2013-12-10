from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Activity, Take, Item
from TakeHelper import TakeHelper

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def redeemActivityCode(request, activityCode):
    success = False
    takeId = ""
    try:
        activity = Activity.objects.get(pk=activityCode)
        success = True
        takeId = TakeHelper.newTake(activity, "Student")
    except Activity.DoesNotExist:
        success = False
    template = loader.get_template('assessments/studentredeem.html')
    context = RequestContext(request, {
        'success': success,
        'takeId': takeId
    })
    return HttpResponse(template.render(context))

def getQuestionPage(request, takeId):
    success = True
    try:
        take = Take.objects.get(pk=takeId)
    except Take.DoesNotExist:
        success = False

    item = ""
    
    if (take.complete == False):
        itemsList = take.activity.itemsList.split(",")
        currentItemId = itemsList[take.currentQuestion]

        try:
            item = Item.objects.get(pk=currentItemId)
        except Item.DoesNotExist:
            success = False


    template = loader.get_template('assessments/take.html')
    context = RequestContext(request, {
        'success': success,
        'takeId': takeId,
        'item': item,
        'currentQuestionNumber': take.currentQuestion+1,
        'complete': take.complete,
        'score': take.currentScore
    })
    return HttpResponse(template.render(context))

def guess(request, takeId):
    guess = request.GET["guess"]

    try:
        take = Take.objects.get(pk=takeId)
    except Take.DoesNotExist:
        pass

    itemsList = take.activity.itemsList.split(",")
    currentItemId = itemsList[take.currentQuestion]

    try:
        item = Item.objects.get(pk=currentItemId)
    except Item.DoesNotExist:
        pass

    correct = False
    feedback = ""
    if (guess == item.correctAns):
        correct = True
        take.currentScore = take.currentScore + 1
    else:
        correct = False
        feedback = item.explanation

    itemsList = take.activity.itemsList.split(",")
    take.currentQuestion = take.currentQuestion+1
    if (take.currentQuestion > len(itemsList)-1):
        take.complete = True
    take.save()
    if correct:
        corstr = "true"
    else:
        corstr = "false"

    return HttpResponse("{\"correct\":\""+corstr+"\", \"feedback\":\""+feedback+"\" }")
