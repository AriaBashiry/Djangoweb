from django import forms

from courses.models import Topic, Episode


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['Title']


class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['Text','Image']