# from .forms import MyForm
from coffee import models, serializers
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from rest_framework import generics


class ExampleHomeView(TemplateView):
    """Home page with links to the examples"""
    template_name = "example_home.html"


#########################################
# Views for Method #1 (Server Side Forms)
#########################################
class ServerSideFormExampleView(FormView):
    template_name = 'server_side_form.html'
    # form_class = MyForm

    def form_valid(self, form):
        # re-render the view instead of redirecting to success_url
        return self.render_to_response(self.get_context_data())


################################
# Views for Method #3 (Vue Form)
################################
class VueFormExampleView(TemplateView):
    template_name = "vue_form_example.html"


class ProductListAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the currently active products.
        """
        return models.Product.objects.filter(is_active=True).order_by('name')
