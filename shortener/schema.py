import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import URL

# Todo: Convert django ORM to graphQl model
class URLType(DjangoObjectType):
    class Meta:
        model = URL

# Todo:  Query all url list        
class Query(graphene.ObjectType):
    urls = graphene.List(URLType, url=graphene.String(),first=graphene.Int(), skip=graphene.Int())
    
    # Todo: Return all url in database
    def resolve_urls(self, info,url=None, first=None, skip=None, **kwargs):
        queryset = URL.objects.all()
        if url:
            _filter = Q(full_url__icontains=url)
            queryset = queryset.filter(_filter)
        
        if first:
            queryset = queryset[:first]
        
        if skip:
            queryset = queryset[skip:]
        
        return queryset
    

#Todo: Create new URL object
class CreateURL(graphene.Mutation):
    url = graphene.Field(URLType)
    
    #Todo: Take graphene string as input
    class Arguments:
        full_url = graphene.String()

    #Todo: Save in ORM database
    def mutate(self, info, full_url):
        url = URL(full_url=full_url)
        url.save()

        return CreateURL(url=url)


class Mutation(graphene.ObjectType):
    create_url = CreateURL.Field()