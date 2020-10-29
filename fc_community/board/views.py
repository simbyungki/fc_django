from django.shortcuts import render
from .models import Board

def board_list(request) :
	board = Board.objects.all().order_by('-id')
	context = {
		'boards': board
	}

	return render(request, 'board/board_list.html', context)