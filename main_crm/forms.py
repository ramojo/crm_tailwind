from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your forms here.
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label=("Email"), widgets=forms.TextInput(attrs={'class': 'border border-solid border-slate-300', 'placeholder': 'Email Address'}), required=True)
    first_name = forms.CharField(max_length=50, widgets=forms.TextInput(attrs={'class': 'border border-solid border-slate-300', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(max_length=50, widgets=forms.TextInput(attrs={'class': 'border border-solid border-slate-300', 'placeholder': 'Last Name'}), required=True)

    class Meta:
        model = User
        # fields = UserCreationForm.Meta.fields + ("email",)
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    # for field in self.fields.values():
    #     field.widget.attrs['class'] = 'border border-solid border-slate-300'
    #     field.widget.attrs['placeholder'] = field.label
    #     field.widget.attrs['required'] = True
    #     field.widget.attrs['autocomplete'] = 'off'
    #     field.widget.attrs['autofocus'] = True
    #     field.widget.attrs['tabindex'] = '1'
    #     field.widget.attrs['maxlength'] = '50'
    #     field.widget.attrs['minlength'] = '3'
    #     field.widget.attrs['pattern'] = '[a-zA-Z0-9]+'
    #     field.widget.attrs['title'] = 'Only letters and numbers are allowed'
    #     field.widget.attrs['oninvalid'] = 'this.setCustomValidity("Please enter a valid ' + field.label + '");' 
    #     field.widget.attrs['oninput'] = 'this.setCustomValidity("");'
    self.fields['username'].widget.attrs['class'] = 'border border-solid border-slate-300'
    self.fields['username'].widget.attrs['required'] = True
    self.fields['username'].widget.attrs['autocomplete'] = 'on'
    self.fields['username'].widget.attrs['autofocus'] = True
    self.fields['username'].label = 'Username'
    self.fields['username'].help_text = 'Please fill in your desired username and make sure it is unique'
    self.fields['username'].widget.attrs['maxlength'] = '50'
    self.fields['username'].widget.attrs['minlength'] = '3'
    self.fields['username'].widget.attrs['pattern'] = '[a-zA-Z0-9]+$'
    self.fields['username'].widget.attrs['title'] = 'Letters, numbers special characters are allowed'
    
    # self.fields['first_name'].widget.attrs['class'] = 'border border-solid border-slate-300'
    # self.fields['first_name'].widget.attrs['required'] = True
    # self.fields['first_name'].widget.attrs['autocomplete'] = 'on'
    # self.fields['first_name'].label = 'First Name'
    # self.fields['first_name'].help_text = 'Please fill in your first name'
    # self.fields['first_name'].widget.attrs['maxlength'] = '50'
    # self.fields['first_name'].widget.attrs['minlength'] = '3'
    # self.fields['first_name'].widget.attrs['pattern'] = '[a-zA-Z]+'
    # self.fields['first_name'].widget.attrs['title'] = 'Only letters are allowed'
    
    # self.fields['last_name'].widget.attrs['class'] = 'border border-solid border-slate-300'
    # self.fields['last_name'].widget.attrs['required'] = True
    # self.fields['last_name'].widget.attrs['autocomplete'] = 'on'
    # self.fields['last_name'].label = 'Last Name'
    # self.fields['last_name'].help_text = 'Please fill in your last name'
    # self.fields['last_name'].widget.attrs['maxlength'] = '50'
    # self.fields['last_name'].widget.attrs['minlength'] = '3'
    # self.fields['last_name'].widget.attrs['pattern'] = '[a-zA-Z]+'
    # self.fields['last_name'].widget.attrs['title'] = 'Only letters are allowed'

    # self.fields['email'].widget.attrs['class'] = 'border border-solid border-slate-300'
    # self.fields['email'].widget.attrs['required'] = True
    # self.fields['email'].widget.attrs['autocomplete'] = 'on'
    # self.fields['email'].label = 'Email Address'
    # self.fields['email'].help_text = 'Please fill in your email address'
    # self.fields['email'].widget.attrs['maxlength'] = '50'
    # self.fields['email'].widget.attrs['minlength'] = '3'
    
    self.fields['password1'].widget.attrs['class'] = 'border border-solid border-slate-300'
    self.fields['password1'].widget.attrs['required'] = True
    self.fields['password1'].widget.attrs['autocomplete'] = 'on'
    self.fields['password1'].label = 'Password'
    self.fields['password1'].help_text = 'Please fill in your password'
    self.fields['password1'].widget.attrs['maxlength'] = '50'
    self.fields['password1'].widget.attrs['minlength'] = '3'
    self.fields['password1'].widget.attrs['pattern'] = '[a-zA-Z0-9]+$'
    self.fields['password1'].widget.attrs['title'] = 'Letters, numbers and special characters are allowed'
    
    self.fields['password2'].widget.attrs['class'] = 'border border-solid border-slate-300'
    self.fields['password2'].widget.attrs['required'] = True
    self.fields['password2'].widget.attrs['autocomplete'] = 'on'
    self.fields['password2'].label = 'Confirm Password'
    self.fields['password2'].help_text = 'Please confirm your password'
    self.fields['password2'].widget.attrs['maxlength'] = '50'
    self.fields['password2'].widget.attrs['minlength'] = '3'
    self.fields['password2'].widget.attrs['pattern'] = '[a-zA-Z0-9]+$'
    self.fields['password2'].widget.attrs['title'] = 'Letters, numbers and special characters are allowed'
    
