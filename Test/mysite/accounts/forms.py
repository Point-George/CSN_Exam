from django import forms
from .models import Registration, Exam

class ExamSelectionForm(forms.Form):
    subject = forms.ChoiceField(choices=[], required=True)
    date = forms.ChoiceField(choices=[], required=True)
    time = forms.ChoiceField(choices=[], required=True)
    location = forms.ChoiceField(choices=[], required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate choices from DB
        self.fields['subject'].choices = [(e.subject, e.subject) for e in Exam.objects.distinct('subject')]
        self.fields['date'].choices = [(e.date, e.date) for e in Exam.objects.distinct('date')]
        self.fields['time'].choices = [(e.time, e.time) for e in Exam.objects.distinct('time')]
        self.fields['location'].choices = [(e.location, e.location) for e in Exam.objects.distinct('location')]
