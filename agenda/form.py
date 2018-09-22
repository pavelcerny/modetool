from django import forms


class NewEntryForm(forms.Form):
    entry_name = forms.CharField(label="Entry Name",
                                 max_length=100,
                                 widget=forms.TextInput(attrs={'placeholder': "eg. Jackson's show"}))


class NewTemplateItemForm(forms.Form):
    item_name = forms.CharField(label="Item Name",
                                max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': "eg. my introduction"}))
