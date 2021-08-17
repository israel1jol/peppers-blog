from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post, Comment, CommentForm, Category


class Index(generic.ListView):
    template_name = 'mainblog/index.html'
    model = Post
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')
    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'mainblog/postdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm
        post = Post.objects.get(slug=self.kwargs['slug'])
        context["comments"] = Comment.objects.filter(post=post)
        context["category"] = Category.objects.get(name=post.category)
        return context

class PostCategory(generic.ListView):
    model = Post
    template_name = 'mainblog/postCategory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(category=self.kwargs['string'])
        context["category"] = Category.objects.get(name=self.kwargs['string'])
        return context
    

def addComment(request, post_slug, *args):
    myform = CommentForm(request.POST)

    if myform.is_valid():
        username = myform.cleaned_data['username']
        email = myform.cleaned_data['email']
        message = myform.cleaned_data['message']
        c = Comment(username=username, email=email, message=message, post=Post.objects.get(slug=post_slug))
        c.save()
        if not args:
            return HttpResponseRedirect(reverse('mainblog:detailpost', args=(post_slug,)))
        return HttpResponseRedirect(reverse('mainblog:categorypost', args=(post_slug, *args,)))

class About(generic.TemplateView):
    template_name = './mainblog/about.html'