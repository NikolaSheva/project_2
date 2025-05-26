from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django.conf import settings
from .models import Post
from django.views.generic import TemplateView, ListView, DetailView
from django.utils import timezone
from .forms import EmailPostForm
from django.shortcuts import get_object_or_404
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        return Post.published.all()


class PublishedView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

def post_share(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} {cd['email']}recommends you read \"{post.title}\""
            message = f"Read \"{post.title}\" at {post_url}\n\n" \
                      f"{cd['name']}'s comments: {cd['comments']}"
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'post/share.html', {'post': post, 'form': form, 'sent': sent})