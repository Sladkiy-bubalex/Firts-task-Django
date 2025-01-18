import debug_toolbar
from django.urls import include, path

from articles.views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
    path('__debug__/', include(debug_toolbar.urls))
]
