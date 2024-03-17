from .import views
from django.urls import path
from rest_framework.routers import DefaultRouter

#it is one of the another method for handling the routers
# router = DefaultRouter()
# router.register(r'sample', views.sample, basename='sample1')
# urlpatterns = router.urls

urlpatterns = [
    #create and list methods implemented in your viewset and only mentioned it, your viewset will only handle POST and GET requests
    path('', views.sample.as_view({'post': 'create', 'get': 'list'}), name='sample'),
    path('user/signup',views.UserSignupViewSet.as_view({'post':'create'}),name='usersignup'),
    path('rider/signup',views.RiderSignupViewSet.as_view({'post':'create'}),name='ridersignup')
]
