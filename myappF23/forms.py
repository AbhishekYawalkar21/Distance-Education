from django import forms
from myappF23.models import Order
from django.forms import ModelForm, RadioSelect, SelectDateWidget

class InterestForm(forms.Form):
    INTEREST_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]

    interested = forms.CharField(
        label='Interested',
        widget=forms.RadioSelect(choices=INTEREST_CHOICES),
        initial=1,
    )

    levels = forms.IntegerField(
        label='Levels',
        min_value=1,
        initial=1,
    )

    comments = forms.CharField(
        label='Additional Comments',
        widget=forms.Textarea,
        required=False,
    )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['student', 'course', 'levels', 'order_date']
        widgets = {'student': RadioSelect,
                   'order_date': SelectDateWidget,
                   }