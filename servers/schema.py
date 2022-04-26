import graphene
from graphene_django.types import DjangoObjectType
from .models import Servers


class ServerType(DjangoObjectType):
    class Meta:
        model = Servers
        fields = ['server_name', 'url', 'port', 'password',
                  'image', 'alt_image', 'description']


class Query(graphene.ObjectType):
    servers = graphene.List(ServerType)

    def resolve_servers(self, info, **kwargs):
        return Servers.objects.all()


schema = graphene.Schema(query=Query)
