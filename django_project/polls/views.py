from django.views.generic import View
# from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

from simple_django_logger.utils import Logger
from simple_django_logger.response import render


class IndexView(View):
    template_name = 'polls/index.html'

    def get(self, request):
        logs = [
            Logger.log_info(request, 'Some info message. For Django render.'),
            Logger.log_debug(request, 'Some debug message. For Django render.'),
            Logger.log_warn(request, 'Some warn message. For Django render.'),
        ]

        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, self.template_name, context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
