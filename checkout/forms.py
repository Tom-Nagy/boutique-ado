from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email','phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county')

    def __init__(self, *args, *kwargs):
        '''
        Add placeholders and classes, remove auto-generated labels
        and set autofocus on hte first field
        '''
        super().__init__(*args, **kwargs)
        # for better ux/ui intead of empty boxes and clunky labels
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': ' Street Address 1',
            'street_address2': ' Street Address 2',
            'county': 'County',
        }

        # set autofocus to full_name field when the page loads for the cursor
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # iterate through the form's field and add a star for required fields
        for field in fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # set the placeholder attr to their values in the dic above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # add a css class
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # remove the form's field label since we use placeholders
            self.fields[field].label = False
