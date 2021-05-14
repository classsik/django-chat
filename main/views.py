from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def room(request, room_name):
    return render(request, 'main/room.html', {
        'room_name': room_name
    })