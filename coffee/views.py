from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from rest_framework.response import Response
from rest_framework.views import APIView

# from .forms import MyForm
# from .models import Article


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


class ItemChoicesView(APIView):
    def get(self, request):
        # articles = Article.objects.all()
        return Response({"articles": 'articles'})
