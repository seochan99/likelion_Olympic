from .models import TalkRoom_Y, TalkRoom_F
from django import forms


class Talking_y(forms.ModelForm):

    class Meta:
        model = TalkRoom_Y
        fields = (
            "author",
            "text"
        )



class Talking_f(forms.ModelForm):
    
    class Meta:
        model = TalkRoom_F
        fields = (
            "author",
            "text"
        )




