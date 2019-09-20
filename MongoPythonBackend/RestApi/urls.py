from django.urls import path
from rest_framework.routers import DefaultRouter
from RestApi import views

router = DefaultRouter()
router.register(r"assays", views.AssayViewSet, basename="assay")
router.register(r"users", views.UserViewSet, basename="user")
urlpatterns = router.urls
