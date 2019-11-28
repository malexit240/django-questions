from django import forms
from .models import Choice

class QuestionForm(forms.Form):
    question_id = forms.IntegerField()

    def celan(self):
        return self.cleaned_data


class ChoiceModelForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['quetion']