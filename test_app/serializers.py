from django.contrib.auth.models import User
from rest_framework import serializers
from test_app.models import Snippet


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(
#                 many=True, read_only=True
#                 )
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')
#
#
# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Snippet
#         fields = ('id', 'owner',
#                   'title', 'code', 'linenos', 'language', 'style')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
            view_name='snippet-highlight', format='html'
            )

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')
        extra_kwargs = {
            'url': {'view_name': 'snippet-detail'},
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
            many=True, view_name='snippet-detail', read_only=True
            )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
