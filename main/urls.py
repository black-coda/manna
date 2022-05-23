from django.urls import path,include
from .views import (index_view, create_manna_view, MannaListView,MannaDetailView,)


urlpatterns = [
   path('', index_view, name='dashboard'),
   path('create/', create_manna_view, name='create-view'),
   path('manna-detail/<slug:slug>/', MannaDetailView.as_view(), name='detail-view'),
   path('manna-list/', MannaListView.as_view(), name='list-view'),
   path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),

   ]


