from .models import *
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    comments=serializers.SerializerMethodField(method_name='get_comments',read_only=True)
    
    class Meta:
        model=Post
        fields='__all__'
    def get_comments(self,obj):
        comment=obj.comments.all()
        serializer=CommentSerializer(comment,many=True)
        return serializer.data
        

 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'