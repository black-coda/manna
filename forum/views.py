from django.shortcuts import render
from .models import Forum, Messages, Topic
from django.views import View


class ForumListView(View):

    def get(self, request, *args, **kwargs):
        forums = Forum.objects.all()
        context = {
            "forums": forums
        }
        return render(request,"forum_list.html", context)


def list_of_forums(request):
    forums = Forum.objects.all()
    context = {
        "forums": forums
    }
    return render(request, "forum_list.html", context)


#TODO: contine from the detail_view
def forum_detail_view(request, forum_slug):
    forum_instance = Forum.objects.get(slug=forum_slug)
    pass
