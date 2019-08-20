"""project_otterside URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout
from django.views.generic import RedirectView
from core import views as core_views

urlpatterns = [
    # Index
    path('', core_views.index, name='index'), 
    path('', RedirectView.as_view(url='/index/', permanent=True)),

    # Snippet List and Detail Views
    path('snippets/', core_views.SnippetListView.as_view(), name='snippets'),
    path('snippets/<int:pk>', core_views.SnippetDetailView.as_view(), name='snippet-detail'),

    # Add, Edit, Delete, and Copy Snippets
    path('add_snippet/', core_views.add_snippet, name='add_snippet'),
    path('edit_snippet/<int:pk>/edit/', core_views.SnippetUpdate.as_view(), name='edit_snippet'),
    path('delete_snippet/<int:pk>/delete', core_views.SnippetDelete.as_view(), name='delete_snippet'),

    # User Page for Snippets
    path('user_page/', core_views.user_view, name='user_page'),

    # Search Results for Snippets
    path('snippets/search', core_views.search_snippets, name = 'search_list'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
