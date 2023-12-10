from django.core.cache.backends.filebased import FileBasedCache
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from blogapp.forms import PostCreateModelForm
from blogapp.models import Post, Tag
from django.core.cache import cache


def post_list_view(request):
    cache = FileBasedCache("file_cache", {})
    post_list = cache.get('post_list')
    tag_list = cache.get('tag_list')
    tag_count = cache.get('tag_count')

    if post_list is None:
        post_list = Post.objects.all()
        tag_list = Tag.objects.all()
        tag_count = Tag.objects.all().count()

        cache.set('post_list', post_list, 10)
        cache.set('tag_list', tag_list, 10)
        cache.set('tag_count', tag_count, 10)

    context = {'post_list': post_list,
               'tag_list': tag_list,
               'tag_count': tag_count}
    return render(request, 'blogapp/post_list.html', context)


def post_list_by_tag_view(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    post_list = Post.objects.filter(tags=tag.pk)
    tag_list = Tag.objects.all()

    context = {'post_list': post_list,
               'tag_list': tag_list}
    return render(request, 'blogapp/post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'blogapp/post_detail.html', context)


def create_post(request):
    context = {'form': PostCreateModelForm()}

    if request.method == 'POST':
        form = PostCreateModelForm(request.POST)
        if form.is_valid():
            form.save()

            cache.delete('post_list')
            cache.delete('tag_list')
            cache.delete('tag_count')

            return redirect('post_list')
        else:
            context['form'] = form

    return render(request, 'blogapp/post_create.html', context)
