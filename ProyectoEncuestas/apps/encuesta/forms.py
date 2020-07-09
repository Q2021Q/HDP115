from django import forms

class TipotrasporteForm(forms.ModelForm):
	class Meta:
		model = Tipotrasporte
		fields = ['tipo', 'iddepartamento']
