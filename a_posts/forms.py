from django import forms
from .models import Post
import requests
from bs4 import BeautifulSoup


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["url", "content", "tags"]
        labels = {
            "content": "Caption",
            "url": "URL",
            "tags": "Tags",
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
            "tags": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "form-control font1",
                }
            ),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        url = self.cleaned_data.get("url")
        try:
            response = requests.get(url, timeout=10)  # Add a timeout to avoid hanging
            if response.status_code == 200:
                source_code = BeautifulSoup(response.text, "html.parser")

                # Extract image URL
                image_meta = source_code.find(
                    "meta",
                    attrs={
                        "property": "og:image",
                        "content": lambda x: x
                        and x.startswith("https://live.staticflickr.com/"),
                    },
                )
                if image_meta:
                    instance.image = image_meta["content"]

                # Extract title
                title_tag = source_code.find("h1", class_="photo-title")
                if title_tag:
                    instance.title = title_tag.get_text(strip=True)

                # Extract artist
                artist_tag = source_code.find("a", class_="owner-name")
                if artist_tag:
                    instance.artist = artist_tag.get_text(strip=True)
        except requests.RequestException as e:
            # Handle exceptions, e.g., log the error or show a message
            print(f"Error fetching URL: {e}")

        if commit:
            instance.save()
            self.save_m2m()
        return instance


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "content",
            "tags",
        ]
        labels = {
            "content": "",
            "tags": "Tags",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-control font1 text-4xl",
                }
            ),
            "tags": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "form-control font1",
                }
            ),
        }
