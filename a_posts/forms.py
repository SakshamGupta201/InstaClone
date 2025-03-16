from django import forms
from .models import Post
from bs4 import BeautifulSoup
import requests


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["url", "content"]
        labels = {
            "content": "Caption",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Add a caption...",
                    "class": "form-control font1 text-4xl",
                }
            ),
            "url": forms.URLInput(
                attrs={
                    "placeholder": "Add url...",
                }
            ),
        }

    def save(self, commit=True):
        instance = super(PostCreateForm, self).save(commit=False)
        url = self.cleaned_data.get("url")
        response = requests.get(url)
        if response.status_code == 200:
            source_code = BeautifulSoup(response.text, "html.parser")
            image_meta = source_code.find(
                "meta",
                attrs={
                    "content": lambda x: x
                    and x.startswith("https://live.staticflickr.com/")
                },
            )
            if image_meta:
                instance.image = image_meta["content"]
            title_tag = source_code.find("h1", class_="photo-title")
            if title_tag:
                instance.title = title_tag.text.strip()
            artist_tag = source_code.find("a", class_="owner-name")
            if artist_tag:
                instance.artist = artist_tag.text.strip()
        if commit:
            instance.save()
        return instance


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "content",
        ]
        labels = {
            "content": "",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-control font1 text-4xl",
                }
            ),
        }
