
from django import forms



class PetitionForm(forms.Form):
    
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=128, label="제목"
    )
    OPTIONS = (
        10,
        25,
        50,
    )
    accept_count = forms.ChoiceField(widget=forms.RadioSelect, choices=OPTIONS)

    contents = forms.CharField(
         error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label="내용"
    )