from django import forms


class AlbumSearchForm(forms.Form):
    album_name = forms.CharField(label='Album Name', max_length=100)
