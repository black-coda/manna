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