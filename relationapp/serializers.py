from rest_framework import serializers
from .models import * 


class AuthorSer(serializers.ModelSerializer):
    book = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Book-detail')
    # book = serializers.StringRelatedField(many=True,read_only=True)
    # book = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # book = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    
    
    class Meta:
        model = Author
        fields = ['id','name','email','gender','book']
    
class BookSer(serializers.HyperlinkedModelSerializer):
   class Meta:
        model = Book
        fields = ['title','auth']
        