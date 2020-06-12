from django import forms
from tweet.models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'messagebox'
        ]


# class TweetForm(forms.Form):
#     tweet = forms.CharField(widget=forms.Textarea, max_length=140)
