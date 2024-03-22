# cookbook/schema.py
import graphene
from graphene_django import DjangoObjectType

from .models import Todo

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo

class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)

    def resolve_todos(self, info):
        return Todo.objects.all()

schema = graphene.Schema(query=Query)