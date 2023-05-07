
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('product',views.ProductView,basename='productview')
urlpatterns = [
    # path('view/<int:id>/',views.ProductView.as_view(),name='product'),
    path('',include(router.urls))


    
]
