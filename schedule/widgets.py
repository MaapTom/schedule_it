from django import forms

class CPFFormatWidget(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': '000.000.000-00', 'pattern': r'\d{3}\.\d{3}\.\d{3}-\d{2}'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)
        pass


class PhoneFormatWidget(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': '(00) 00000-0000', 'pattern': r'\(\d{2}\) \d{5}-\d{4}'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)
