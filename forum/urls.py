from django.urls import path
from .views import list_of_forums, ForumListView

urlpatterns = [
    path("", ForumListView.as_view())
]
