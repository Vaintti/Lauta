from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Board


def index(request):
    boards = Board.objects.order_by('url')
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


def board(request, url):
    item = get_object_or_404(Board, url=url)
    return render(request, 'boards/board.html', {'board': item})
