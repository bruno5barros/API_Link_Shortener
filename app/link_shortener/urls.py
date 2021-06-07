from django.urls import path, include
from rest_framework.routers import DefaultRouter
from link_shortener import views


router = DefaultRouter()
router.register('linkshorteners', views.LinkShortenerViewSet)

app_name = 'link_shortener'

urlpatterns = [
    path('', include(router.urls)),
    path('<str:hash>/', views.ValidateShortedLink.as_view(), name='ValidateShortedLink')
    # path(r'^.*', views)
]
