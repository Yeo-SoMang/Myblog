from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from rest_framework.parsers import JSONParser

from blog.models import Post


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['contents'] = Post.objects.select_related('user')
        user = self.request.user
        return  context


def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    context = {
        'post' : post
    }
    return render(request, 'post_detail.html', context)

