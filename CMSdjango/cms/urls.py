from django.urls import path
from . import views

urlpatterns = [
    # Leave as empty string for base url
    # path('',views.Catalog, name="Catalog"),
    path('CC',views.CC, name="CC"),
    path('CO',views.CO, name="CO"),
    path('Update_Profile',views.Update_Profile, name="Update_Profile"),
    path('Preview',views.Preview, name="Preview"),
    path('',views.secsignin, name="secsignin"),
    path('register',views.register, name="register"),
    path('display',views.display, name="display"),
    path('Catalog',views.Catalog, name="Catalog")


]