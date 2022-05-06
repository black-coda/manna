from django.urls import path
from .views import index_view, create_manna_view, MannaListView, manna_detail_view


urlpatterns = [
   path('', index_view, name='dashboard'),
   path('create/', create_manna_view, name='create-view'),
   path('manna-list/<slug>/', manna_detail_view, name='detail-view'),
   path('manna-list/', MannaListView.as_view(), name='list-view'),]


