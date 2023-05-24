from django import forms


class GeoForm(forms.Form):
    projection_plane = forms.CharField()
    coordinates = forms.CharField()

    def clean_projection_plane(self):
        projection_plane = self.cleaned_data['projection_plane'].lower()
        if projection_plane not in (['xy', 'yz', 'xz']):
            raise forms.ValidationError("Invalid projection plane")
        return projection_plane
