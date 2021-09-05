from django import  forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=220)
    password = forms.CharField(max_length=220, widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data

        username = data.get('username')
        password = data.get('password')

        # (optional) login for custom validation
        return data
