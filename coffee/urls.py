from coffee import views
from django.urls import path

app_name = "coffee"
urlpatterns = [
    path('', views.ExampleHomeView.as_view(), name='index'),
    # METHOD #1 (Server Side Form) URLS
    path('server-side-form-example/', views.ServerSideFormExampleView.as_view(), name='server_side_form_example'),
    # METHOD #3 (Vue Form) URLS
    path('vue-form-example/', views.VueFormExampleView.as_view(), name='vue_form_example'),
]
