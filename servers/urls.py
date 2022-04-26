from django.urls import path
from graphene_django.views import GraphQLView
from servers.schema import schema

urlpatterns = [
    path('servers', GraphQLView.as_view(graphiql=True, schema=schema)),
]
