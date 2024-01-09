from django.conf import settings
from django.contrib import admin
from django.urls import path
import blog.views
import authentication.views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', blog.views.home, name='home'),
    path('signup/', authentication.views.Signup_page, name='signup'),
    path('photo/upload/', blog.views.photo_upload, name='photo_upload'),
    path('blog/created/', blog.views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:blog_id>', blog.views.view_blog, name='view_blog'),
    path('blog/upload-multiple/', blog.views.create_multiple_photos, name='create_multiple_photos'),
    path('blog/<int:blog_id>/edit', blog.views.edit_blog, name='edit_blog'),
    path('', LoginView.as_view(template_name='authentication/login.html',
                               redirect_authenticated_user=True),
         name='login'),
    path('profile-photo/upload', authentication.views.upload_profile_photo,
         name='upload_profile_photo'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
