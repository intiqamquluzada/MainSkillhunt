from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Blog, Comment


#
# def blog(request):
#
#     return render(request, 'blog.html')
# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'blog-single.html'
#
#     def get_context_data(self, **kwargs):
#         context = {
#             'blog': Blog.objects.filter(slug=self.kwargs['slug']),
#         }
#         return context


def bl_detail(request, slug):
    blog = Blog.objects.filter(slug=slug)
    comment = Comment.objects.filter(blog__slug=slug)
    query = request.GET.get('q')
    if query:
        comment = comment.filter(Q(name__icontains=query) |
                                 Q(message__icontains=query) |
                                 Q(email__icontains=query) |
                                 Q(website__icontains=query)
                                 )
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = CommentForm()
    else:
        form = CommentForm()

    context = {
        'blog': blog,
        'comment': comment,
        'form': form
    }
    return render(request, 'blog-single.html', context=context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        blogall = Blog.objects.all()
        context = {
            'blogall': blogall
        }
        return context

# def blog_details(request,slug):
#     comment = Comment.object.filter()
#     return render(request, 'blog-single.html')
