from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your forms here.
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email Address'}), required=True)
    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={ 'autofocus': 'True', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), required=True)

    class Meta:
        model = User
        # fields = UserCreationForm.Meta.fields + ("email",)
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    # self.fields['username'].widget.attrs['class'] = 'mb-5'
    self.fields['username'].widget.attrs['required'] = True
    self.fields['username'].widget.attrs['autocomplete'] = 'on'
    self.fields['username'].label = ''
    self.fields['username'].widget.attrs['placeholder'] = 'Please fill in your desired username and make sure it is unique'
    self.fields['username'].widget.attrs['maxlength'] = '50'
    self.fields['username'].widget.attrs['minlength'] = '3'
    self.fields['username'].widget.attrs['pattern'] = '[a-zA-Z0-9]+$'
    
    # self.fields['password1'].widget.attrs['class'] = 'mb-5'
    self.fields['password1'].widget.attrs['required'] = True
    self.fields['password1'].widget.attrs['autocomplete'] = 'on'
    self.fields['password1'].label = ''
    self.fields['password1'].widget.attrs['placeholder']  = 'Please create a password'
    self.fields['password1'].widget.attrs['maxlength'] = '50'
    self.fields['password1'].widget.attrs['minlength'] = '3'
    self.fields['password1'].widget.attrs['pattern'] = '[a-zA-Z0-9]+$'
    # self.fields['password1'].widget.attrs['title'] = 'Letters, numbers and special characters are allowed'
    
    # self.fields['password2'].widget.attrs['class'] = 'mb-5'
    self.fields['password2'].widget.attrs['required'] = True
    self.fields['password2'].widget.attrs['autocomplete'] = 'on'
    self.fields['password2'].label = ''
    # self.fields['password2'].help_text = 'Please confirm your password'
    self.fields['password2'].widget.attrs['maxlength'] = '50'
    self.fields['password2'].widget.attrs['minlength'] = '3'
    self.fields['password2'].widget.attrs['pattern'] = '[a-zA-Z0-9]+$'
    self.fields['password2'].widget.attrs['placeholder'] = 'Please confirm your password'
    # self.fields['password2'].widget.attrs['title'] = 'Letters, numbers and special characters are allowed'
    
