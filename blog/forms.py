from django . forms import ModelForm
from .models import  Customers

class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'