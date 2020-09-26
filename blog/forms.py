from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.Textarea)
    # -> by doing this we can manipulate our model's data type
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']

    def clean_title(self, *args, **kwargs):
        print("MODEL = ", dir(self))
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)  # __iexact makes it case insensetive
        if self.instance is not None:
            print("PK = ", self.instance.pk)
            qs = qs.exclude(pk=self.instance.pk)
        print(qs)
        if qs.exists():
            raise forms.ValidationError("Title {title} Already Exist".format(title=title))
        return title
