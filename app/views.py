from django.shortcuts import render,get_object_or_404
from .models import *
from rest_framework import status,permissions,generics,viewsets
from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import action,api_view
# Create your views here.

@api_view(['GET'])
def get_user_posts(request):
    try:
        posts=Post.objects.filter(created_by=request.user)
        responde=PostSerializer(posts,many=True)
        return Response({"details":responde.data})
    except (TypeError,AttributeError,AssertionError):
        return Response({"error":"no Result something wrong in this request"})
        
class PoststView(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field='id'
    def perform_create(self, serializer):
        created_by=self.request.user
        return serializer.save(created_by=created_by)
    

class CommentView(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    lookup_field='id'
    # @action(detail=True ,methods=['post'])
    def create(self,request, *args, **kwargs):
        id=self.kwargs['id']
        user=self.request.user
        post=get_object_or_404(Post,id=id)
        text=request.data['text']
        comment=Comment.objects.create(post=post,user=user,text=text)
        comment.save()
        
        responde=PostSerializer(post,many=False)
        return Response({"details":responde.data})
    def update(self, request, *args, **kwargs):
        id=self.kwargs['id']
        data=request.data
        user=request.user
        post=get_object_or_404(Post,id=id)
        text=data['text']
        comment=get_object_or_404(Comment,user=user,id=id)
        if comment:
            
            comment.text=text
            comment.save()
            responde=PostSerializer(post,many=False)
            return Response({"details":responde.data})
        else:


           return Response({"error":"no comments found"})
        
    def destroy(self, request, *args, **kwargs):
        id=self.kwargs['id']
        
        user=request.user
        try:

            comment=get_object_or_404(Comment,user=user,id=id)
        

            if comment and comment.user==user:
                
                comment.delete()
                
            
                return Response({"details":"comment deleted"})
            else:


                return Response({"error":"no comments found"})
        except (KeyError,TypeError):
            return Response({"error":"nonono"})
     
       