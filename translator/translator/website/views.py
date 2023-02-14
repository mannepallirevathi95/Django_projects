from .models import Post
from django.views import generic
# Create your views here.

class WebsiteView(generic.DetailView):
    model = Post
    template_name = 'website.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'