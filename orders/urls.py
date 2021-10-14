
from django.urls import path,include
from . import views


urlpatterns = [
    path('v1/order/', views.OrderAPIView.as_view(), name="orders"),
    path('<int:id>', views.OrderDetailAPIView.as_view(), name="order"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]