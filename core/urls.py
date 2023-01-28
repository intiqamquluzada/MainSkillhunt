from django.urls import path

from core.views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),

    path('browsejobs', BrowseJobsView.as_view(), name='browsejobs'),

    path('candidates', CandidatesListView.as_view(), name='candidates'),
    path('contact', contact, name='contact'),
    path('job-post', job_post, name='job_post'),
    path('new-post', new_post, name='new_post'),
    path('candidate-detail<slug:slug>', CandidateDetailView.as_view(), name='candidate_detail')
]
