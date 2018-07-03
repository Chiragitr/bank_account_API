from django.conf.urls import url, include
from rest_framework import routers
from urcashback.bank_account import views

router = routers.DefaultRouter()
router.register(r'bank', views.BankViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]