from base.models.notes import Note
from base.serializers.notes_serializer import NoteSerializer
from rest_framework.response import Response
from rest_framework import status


def getNotesList(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)

def getNoteDetail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note)

    return Response(serializer.data)

def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data, many=False)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    
    return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')