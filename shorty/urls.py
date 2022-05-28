
from django.contrib import admin
from django.urls import path
# Todo: GraphQL and Cross-Site Request
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
# Todo: Shortner URL redirect
from shortener.views import root

urlpatterns = [
    path('admin/', admin.site.urls),
    #! GraphQL Endpoint
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('<str:url_hash>/', root, name='root'),
]
