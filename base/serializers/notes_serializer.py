from rest_framework.serializers import ModelSerializer
from base.models.notes import Note


class NoteSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'