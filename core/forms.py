from django import forms
from .models import CustomUser, Liability, OweOver


class CustomUserForm(forms.ModelForm):

	class Meta:
		model = CustomUser
		exclude = ['last_login']
		widgets = {
	            'email'   : forms.EmailInput(attrs={'class' : 'form-control emailctn'}),
	            'full_name'   : forms.TextInput(attrs={'class' : 'form-control emailctn'}),
	            'mobile_number'   : forms.TextInput(attrs={'class' : 'form-control emailctn'}),
	            'password'   : forms.PasswordInput(attrs={'class' : 'form-control emailctn'})
	        }


class LoginForm(forms.Form):
	email = forms.CharField(
		max_length=255,
		widget=forms.EmailInput(
			attrs={'class' : 'form-control emailctn'}
		)
	)
	password = forms.CharField(
		max_length=255,
		widget=forms.PasswordInput(
			attrs={'class' : 'form-control emailctn'}
		)
	)


class LiabilityForm(forms.ModelForm):

	class Meta:
		model = Liability
		# fields = '__all__'
		exclude = ['user', 'owe_over']
		widgets = {
			'expense'   : forms.NumberInput(attrs={'class' : 'form-control emailctn'}),
			'expense_type'   : forms.Select(attrs={'class' : 'form-control emailctn'}),
			'spent_in_ownself'   : forms.NumberInput(attrs={'class' : 'form-control emailctn'}),
			# 'user'   : forms.TextInput(attrs={'class' : 'form-control emailctn'}),
			# 'owe_over'   : forms.TextInput(attrs={'class' : 'form-control emailctn'}),
		}


class OweForm(forms.ModelForm):

	class Meta:
		model = OweOver
		fields = '__all__'
		widgets = {
			'user_owes'   : forms.Select(attrs={'class' : 'form-control emailctn'}),
			'percent_value' : forms.NumberInput(attrs={'class' : 'form-control emailctn'}),
			'amount'   : forms.NumberInput(attrs={'class' : 'form-control emailctn'}),
		}




