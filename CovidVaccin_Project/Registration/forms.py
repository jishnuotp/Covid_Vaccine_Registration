from django import forms

from .models import Person, Vaccine_Center


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['First_Name','Last_name','Email','Address','Contact_Number','Age','district','vaccine_center','Created_by']
        widgets = { 'Created_by': forms.HiddenInput(),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vaccine_center'].queryset = Vaccine_Center.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['vaccine_center'].queryset = Vaccine_Center.objects.filter(District_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['vaccine_center'].queryset = self.instance.district.vaccine_center_set.order_by('name')