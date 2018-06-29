from django import forms


class login(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username','password']

        widgets = {
            'password':forms.PasswordInput(),
        }


class register(forms.ModelForm):

    class Meta:

        model = UserDetail
        fields = ['user','firstName','lastName','address','contactNum']