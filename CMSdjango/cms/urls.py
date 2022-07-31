from django.urls import path
from . import views

app_name = "cms"

urlpatterns = [
    # Leave as empty string for base url
    # path('',views.Catalog, name="Catalog"),
    path('CC',views.CC, name="CC"),
    path('CO',views.CO, name="CO"),
    path('<int:user_id>/',views.Update_Profile, name="Update_Profile"),
    path('Preview',views.Preview, name="Preview"),
    path('',views.secsignin, name="secsignin"),
    path('register',views.register, name="register"),
    # path('<int:User_id>/',views.display, name="display"),
    path('Catalog',views.Catalog, name="Catalog")


]