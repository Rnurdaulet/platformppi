from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("select2/", include("django_select2.urls")),
    path("", include("apps.lookups.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path("privacy", lambda request: render(request, "privacy.html"), name="privacy"),
    path("404", lambda request: render(request, "404.html"), name="404"),
    path("", include("apps.accounts.urls")),
    path("contest/", include("apps.contest.urls", namespace="contest")),
)
