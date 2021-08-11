from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/', include('book_club.account.urls')),
    path('', include('book_club.user_profile.urls')),
    path('events/', include('book_club.book_event.urls')),
    path('books/', include('book_club.book.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
