from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin) :
	list_display = ('subject', 'writer', 'registered_dtm')

admin.site.register(Board, BoardAdmin)

