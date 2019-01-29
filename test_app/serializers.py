from django.contrib.auth.models import User
from rest_framework import serializers
from test_app.models import Snippet

#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
                many=True, queryset=Snippet.objects.all()
                )

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('__all__')
