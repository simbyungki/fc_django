from django.shortcuts import render, redirect
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm


def board_write(request) : 
	if request.method == 'POST' :
		form = BoardForm(request.POST)
		if form.is_valid() :
			user_id = request.session.get('user')
			fcuser = Fcuser.objects.get(pk=user_id)
			board = Board()
			board.subject = form.cleaned_data['subject']
			board.contents = form.cleaned_data['contents']
			board.writer = fcuser
			board.save()
			return redirect('board/list')
	else :
		form = BoardForm()

	return render(request, 'board/board_write.html', {'form': form})

def board_list(request) :
	board = Board.objects.all().order_by('-id')
	context = {
		'boards': board
	}

	return render(request, 'board/board_list.html', context)
