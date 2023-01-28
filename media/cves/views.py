from django.shortcuts import render
from django.views.generic import ListView

from core.models import Candidate


def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog-single.html')


def browsejobs(request):
    return render(request, 'browsejobs.html')


def contact(request):
    return render(request, 'contact.html')


def job_post(request):
    return render(request, 'job-post.html')


def new_post(request):
    return render(request, 'new-post.html')





class CandidatesView(ListView):
    model = Candidate
    paginate_by = 6
    template_name = 'candidates.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'worker': Candidate.objects.all()
        }
        return context
