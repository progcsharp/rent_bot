from django.forms import ModelForm
from django import forms

from .models import TgUser, Info


class ModerForm(ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(attrs={"id":"editUserId"}))
    name = forms.CharField(required=False, max_length=2500, widget=forms.TextInput(attrs={"id":"editUserName"}))
    discount = forms.CharField(required=False, max_length=2500, widget=forms.TextInput(attrs={"id":"editUserStock"}))
    traffic = forms.CharField(required=False, max_length=2500, widget=forms.TextInput(attrs={"id":"editUserValue"}))
    password = forms.CharField(max_length=2500, widget=forms.TextInput(attrs={"id":"editUserPass"}))
    cart = forms.CharField(required=False, max_length=2500, widget=forms.TextInput(attrs={"id":"editUserCard"}))
    bonus = forms.IntegerField(widget=forms.TextInput(attrs={"id":"editUserBonuses"}), initial=0)

    class Meta:
        model = TgUser
        fields = ["id", "name", "password", "cart", "traffic", "discount", "bonus"]


class AddModerForm(ModelForm):
    name = forms.CharField(required=False, max_length=2500, widget=forms.TextInput(attrs={"id":"AddUserName"}))
    discount = forms.CharField(required=False, max_length=2500, widget=forms.TextInput(attrs={"id":"AddUserStock"}))
    traffic = forms.CharField(required=False, max_length=2500, widget=forms.TextInput(attrs={"id":"AddUserValue"}))
    password = forms.CharField(max_length=2500, widget=forms.TextInput(attrs={"id":"AddUserPass"}))
    cart = forms.CharField(required=False, max_length=2500, widget=forms.TextInput(attrs={"id":"AddUserCard"}))
    bonus = forms.IntegerField(widget=forms.TextInput(attrs={"id":"AddUserBonuses"}), initial=0)

    class Meta:
        model = TgUser
        fields = ["name", "password", "cart", "traffic", "discount", "bonus"]


class SearchModerForm(ModerForm):
    name = forms.CharField(required=False, max_length=2500, widget=forms.TextInput(attrs={"placeholder":"Поиск по ФИО"}))
