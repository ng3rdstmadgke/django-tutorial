from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import Http404, HttpResponse

from polls.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    # ショートカットなしのテンプレート描画
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    # ショートカットを利用したテンプレート描画
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    # pkが存在しない場合に404を返す
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exists")

    # pkが存在しない場合に404を返す (ショートバージョン)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = f"You'relooking at the results of question {question_id}"

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
