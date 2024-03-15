from django.http import HttpResponse
from django.shortcuts import render, redirect

from base.forms import RoomForm
from base.models import Room

# rooms = [
#     {'id': 1, 'name': 'Lets learn python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Lets learn Java'},
#     {'id': 4, 'name': 'Lets learn JavaScript'},
# ]

def home(request):

    rooms = Room.objects.all()

    context = { 'rooms': enumerate(rooms, start=1) }

    return render(request, 'base/home.html', context)

def room(request, pk):
    
    room = Room.objects.get(id=pk)

    context = {'room': room}

    return render(request, 'base/room.html', context)

def createRoom(request):

    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)

    form = RoomForm(instance=room)

    context = {'form': form }
    return render(request, 'base/room_form.html', context)