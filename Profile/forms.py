from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    #define the meta data that defines
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
                )
        def save(self, commit = True):
            user = super(RegistrationForm, self).save(commit=False) # dont save it just yet because
            user.first_name = self.cleaned_data['first_name'] # now safe to store in the db
            user.first_name = self.cleaned_data['last_name'] # now safe to store in the db
            user.first_name = self.cleaned_data['email'] # now safe to store in the db
            # check above

            if commit:
                user.save()
            return user

