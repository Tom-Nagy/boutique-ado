from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        '''
        Add placeholders and classes, remove auto-generated labels
        and set autofocus on the first field
        '''
        super().__init__(*args, **kwargs)
        # for better ux/ui instead of empty boxes and clunky labels
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # set autofocus to full_name field when the page loads for the cursor
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        # iterate through the form's field and add a star for required fields
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # set the placeholder attr to their values in the dic above
                self.fields[field].widget.attrs['placeholder'] = placeholder
                # add a css class
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            # remove the form's field label since we use placeholders
            self.fields[field].label = False
