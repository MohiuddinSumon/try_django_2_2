from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm


# Create your views here.


def detail_blog_page_by_id(request, post_id):
    template_name = 'blog/detail.html'
    # obj = BlogPost.objects.get(id=post_id)
    obj = get_object_or_404(BlogPost, id=post_id)
    context = {"Object": obj, "method": "ID"}
    return render(request, template_name, context)


def detail_blog_page_by_slug(request, slug):
    template_name = 'blog/detail.html'
    try:
        obj = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        raise Http404
    context = {"Object": obj, "method": "Slug"}
    print("Django Says", request.method, request.path, request.user)
    return render(request, template_name, context)


def blog_post_list_view(request):
    # List out objects
    title = "Blog Lists"
    query_set = BlogPost.objects.all()
    template_name = "blog/list.html"
    context = {"object_list": query_set, "title": title}
    return render(request, template_name, context)


def blog_post_create_view(request):
    title = "Blog Create"
    template_name = "blog/create.html"
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostForm()

        """
            we could also used something like this: 
            title = form.cleaned_data['title']
            obj = BlogPost()
            obj.title = title
            obj.save
            
            or we can use django's built in method for that
            obj = BlogPost.object.create(title=title)
            
            but in our case we used **form.cleaned_date -> 
            this makes a dictionary like -> {'title': 'Test', 'slug': 'test02', 'content': 'testing saving'}
            and pass argument as key value pair and creates the object
            
        """
    context = {
        'form': form,
        "title": title
    }
    return render(request, template_name, context)


def blog_post_create_model_view(request):

    print(request.POST)
    form = BlogPostModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        # just calling save will create the objects
        """
            obj = form.save(commit=False) 
            this will not save the object rather return to obj variable, we can manipulate it and save 
            
            obj.title = form.cleaned_data.get("title") + "Modified Value"
            obj.save()
        """
        form = BlogPostModelForm()

    title = "Blog Create with model form"
    template_name = "blog/create.html"
    context = {
        'form': form,
        "title": title
    }
    return render(request, template_name, context)

def blog_post_retrieve_view(request, slug):
    # 1 object -> detail view
    title = "Blog Detail"
    template_name = 'blog/detail.html'
    try:
        obj = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        raise Http404
    context = {"Object": obj, "method": "Slug", "title": title}
    print("Django Says", request.method, request.path, request.user)
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    title = "Blog Update"
    template_name = 'blog/update.html'
    try:
        obj = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        raise Http404
    context = {"Object": obj, "method": "Slug", 'form': None, "title": title}
    print("Django Says", request.method, request.path, request.user)
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    title = "Blog Delete"
    template_name = 'blog/delete.html'
    try:
        obj = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        raise Http404
    context = {"Object": obj, "method": "Slug", 'form': None, "title": title}
    print("Django Says", request.method, request.path, request.user)
    return render(request, template_name, context)
