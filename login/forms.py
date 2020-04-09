from django import forms

from .models import Login

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length = 120)
    password = forms.CharField(max_length = 32)

    class Meta:
        model = Login
        fields = [
            'username',
            'password',
        ]
"""
    def clean_username(self):
        user = self.cleaned_data.get("username")
        pass_word = self.cleaned_data.get("password")
        print(self.cleaned_data)
        logins = Login.objects.all()
        count=0
        for i in range(len(logins)):
            #print(logins[i])
            if(user == logins[i].username):
                count=count+1
                break;
        if(count==1):
            return i
        else:
            raise forms.ValidationError("Username/password is invalid.")

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        if not self.username.check_password(password):
            raise ValidationError('Password is invalid.')
        pass_word = self.cleaned_data.get("password")
        logins = Login.objects.all()
        #print(self.cleaned_data)
        return pass_word
        
        if(pass_word == logins[i].password):
            return pass_word
        else:
            #print(pass_word)
            #print('gotten:' + logins[i].password)
            raise forms.ValidationError("password is invalid.")
        """
        