import graphene
from graphene_django import DjangoObjectType

from .models import Platform


class PlatformType(DjangoObjectType):
    class Meta:
        model = Platform


class Query(graphene.ObjectType):
    platforms = graphene.List(PlatformType)

    def resolve_platforms(self, info, **kwargs):
        return Platform.objects.all()


# Platform Creating Mutation
class CreatePlatform(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    name = graphene.String()
    phone = graphene.String()
    email = graphene.String()
    connection_date = graphene.Date()

    class Arguments:
        url = graphene.String()
        name = graphene.String()
        phone = graphene.String()
        email = graphene.String()
        connection_date = graphene.Date()

    def mutate(self, info, url, name, phone, email, connection_date):
        platform = Platform(url=url, name=name, phone=phone, email=email, connection_date=connection_date)
        platform.save()

        return CreatePlatform(
            id=platform.id,
            url=platform.url,
            name=platform.name,
            phone=platform.phone,
            email=platform.email,
            connection_date=platform.connection_date,
        )


class Mutation(graphene.ObjectType):
    create_platform = CreatePlatform.Field()