from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from happyfeet import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^login/$', auth_views.login, name='login'),
url(r'^logout/$', auth_views.logout, name='logout'),


url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/profile')),
url('^profile/', CreateView.as_view(
                    template_name='profile.html',
                    form_class=UserCreationForm,)),

url('^closet/', views.get_closet, name='closet'),
url('^home/', views.open_home, name='home'),
url('^$', views.open_home, name='home'),
url('^shoe/new/$', views.create_shoe, name='addshoe'),

url(r'^shoe/([0-9]+)/$', views.select_shoe, name='selectshoe'),
url(r'^shoe/([0-9]+)/edit/', views.add_miles, name='addmiles'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
