from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.db.models import Q
from core.forms import JobPostForm, ContactForm
from core.models import BrowseJobs, Candidates, JobPost

XLA = (
    ('bachelor', 'Bachelor'),
    ('master', 'Master'),
    ('doctor', 'Doctorant'),
    ('noedu', 'No education')
)

CHOICES = (
    ('full_time', 'Full time'),
    ('part_time', 'Part time'),
    ('freelance', 'Freelance'),
    ('internship', 'Internship'),
    ('termporary', 'Termporary')
)


def index(request):
    job = JobPost.objects.all()
    query_title = request.GET.get('q')
    query_type = request.GET.get('type')
    query_location = request.GET.get('ql')
    if query_location or query_type or query_title:
        if query_title:
            job = job.filter(
                Q(title__icontains=query_title)
            )
        if query_type:
            job = job.filter(
                Q(job_type__in=query_type)
            )
        if query_location:
            job = job.filter(
                Q(location__icontains=query_location)
            )
        context = {
            'job': job,
            'job_type': CHOICES,
        }
        return render(request, 'browsejobs.html', context)

    context = {
        'choice_type': CHOICES,

    }
    return render(request, 'index.html', context)


# def browsejobs(request):
#     info = BrowseJobs.objects.all()
#     context = {
#         'info': info
#     }
#     return render(request, 'browsejobs.html', context)


class BrowseJobsView(ListView):
    model = JobPost
    template_name = 'browsejobs.html'

    def get(self, request, *args, **kwargs):
        job = JobPost.objects.all()
        query_search = request.GET.get('q')
        query_category = request.GET.getlist('job')
        query_type = request.GET.getlist('type')

        if query_search or query_category or query_type:
            if query_search:
                job = job.filter(
                    Q(title__icontains=query_search)
                )
            if query_category:
                job = job.filter(
                    Q(title__in=query_category)
                )

            if query_type:
                job = job.filter(
                    Q(job_type__in=query_type)
                )

        context = {
            'job': job,
            'job_type': CHOICES,
        }
        return render(request, 'browsejobs.html', context=context)


# def candidates(request):
#     context = {
#         'cand': Candidates.objects.all()
#     }
#     return render(request, 'candidates.html', context=context)


class CandidatesListView(ListView):
    model = Candidates
    template_name = 'candidates.html'
    paginate_by = 2
    queryset = Candidates.objects.all()
    context_object_name = 'cand'

    # def get(self, request, *args, **kwargs):
    #     p = request.GET.get('page')
    #     x = Candidates.objects.all()
    #     a = Paginator(x, 3)
    #     try:
    #         post = a.page(p)
    #     except PageNotAnInteger:
    #         post = a.page(1)
    #     context = {
    #         'cr': CHOICES,
    #         'cand': a
    #     }
    #     return render(request, 'candidates.html', context)


# def candidate_detail(request, id):
#     candidate = Candidates.objects.filter(id=id)
#     context = {
#         'candidate': candidate
#     }
#     return render(request, 'candidates-detail.html', context=context)


class CandidateDetailView(DetailView):
    model = Candidates
    template_name = 'candidates-detail.html'

    def get_context_data(self, **kwargs):
        context = {
            'candidate': Candidates.objects.filter(slug=self.kwargs['slug'])
        }
        return context


def contact(request):
    if request.method == 'POST':
        form2 = ContactForm(request.POST)
        if form2.is_valid():
            form2.save()
            form2 = ContactForm()
    else:
        form2 = ContactForm()
    context = {
        'form2': form2
    }
    return render(request, 'contact.html', context=context)


def job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = JobPostForm()
    else:
        form = JobPostForm()
    context = {
        'form': form
    }
    return render(request, 'new-post.html', context=context)


def new_post(request):
    return render(request, 'job-post.html')
