# -*- coding: utf-8 -*-
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, 世豪汇科智能科技！")
