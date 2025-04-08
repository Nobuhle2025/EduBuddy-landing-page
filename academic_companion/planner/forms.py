from django import forms
from .models import Assignment
from .models import ClassSchedule


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'deadline', 'completed']  # Add 'completed' to the fields
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'completed': forms.CheckboxInput()  # Optional: You can customize the checkbox input widget
        }



class ReminderForm(forms.Form):
    reminder = forms.CharField(widget=forms.Textarea, label="Reminder Message")
    reminder_date = forms.DateField(widget=forms.SelectDateWidget(), label="Reminder Date")
    reminder_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Reminder Time")




class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['class_name', 'class_day', 'class_time_start', 'class_time_end', 'instructor_name', 'location', 'notes']

