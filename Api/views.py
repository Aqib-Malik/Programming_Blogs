import email
from unicodedata import category
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import generics, permissions
from knox.models import AuthToken

class ProfileViewset(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer 

# class ProfiletwoViewset(viewsets.ModelViewSet):
#     queryset=Profile.objects.all()
#     serializer_class=ProfileTeoSerializer 
class ProfiletwoViewset(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def get(self, request,cid=None):
        userData=User.objects.filter(id=cid)
        query=Profile.objects.filter(user=cid)
        serialize=ProfileTeoSerializer(query,many=True)
        return Response(serialize.data)

class PostViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer 



#Post Api
# class PostView(APIView):
#     # permission_classes=[all]
#     # authentication_classes=[TokenAuthentication]
#     def get(self, request):
        
#         query=Post.objects.all()
#         serialize=PostSerializer(query,many=True)
#         data=[]
#         for post in serialize.data:
#             # #######Likes
#             # post_like=Likes.objects.filter(post=post['id']).filter(like=True).count()
#             # ####checking me like or not
#             # myLikes=Likes.objects.filter(post=post['id']).filter(user=request.user).first()
#             print(post['id'])
#             post_like=Likes.objects.filter(post=post['id']).filter(like=True).count()
#             print(post_like)
#              #######Comments
#             comment_query=Comment.objects.filter(post=post['id'])
#             comment_serializer=CommentSerializer(comment_query,many=True)
#             post['comment']=comment_serializer.data
#             comment_data=[]
#             for comment in comment_serializer.data:
#                 reply_query=Reply.objects.filter(comment=comment['id'])
#                 reply_serializer=ReplytSerializer(reply_query,many=True)
#                 comment['reply']=reply_serializer.data
#                 comment_data.append(comment)
            
#             data.append(post)
#         post['totalLikes']=post_like
#         print(data[0]['id'])

#         # data=[]
#         # for post in serialize.data:
#         #     #######Likes
#         #     post_like=Likes.objects.filter(post=post['id']).filter(like=True).count()
#         #     ####checking me like or not
#         #     myLikes=Likes.objects.filter(post=post['id']).filter(user=request.user).first()
#         #     if myLikes:
#         #         post['like']=myLikes.like
#         #     else:
#         #         post['like']=False
#         #     post['totalLikes']=post_like
#             # #######Comments
#             # comment_query=Comment.objects.filter(post=post['id'])
#             # comment_serializer=CommentSerializer(comment_query,many=True)
#             # post['comment']=comment_serializer.data
#         #     #######Reply
#         #     comment_data=[]
#         #     for comment in comment_serializer.data:
#         #         reply_query=Reply.objects.filter(comment=comment['id'])
#         #         reply_serializer=ReplytSerializer(reply_query,many=True)
#         #         comment['reply']=reply_serializer.data
#         #         comment_data.append(comment)

#         #     data.append(post)

#         return Response(serialize.data)

# Post Api
class PostView(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def get(self, request):
        query=Post.objects.all()
        serialize=PostSerializer(query,many=True)
        data=[]
        for post in serialize.data:
            #######Likes
            post_like=Likes.objects.filter(post=post['id']).filter(like=True).count()
            ####checking me like or not
            # myLikes=Likes.objects.filter(post=post['id']).filter(user=request.user).first()
            # # if myLikes:
            # #     post['like']=myLikes.like
            # # else:
            # #     post['like']=False
            post['totalLikes']=post_like
            #######Comments
            comment_query=Comment.objects.filter(post=post['id'])
            comment_serializer=CommentSerializer(comment_query,many=True)
            post['comment']=comment_serializer.data
            #######Reply
            comment_data=[]
            for comment in comment_serializer.data:
                reply_query=Reply.objects.filter(comment=comment['id'])
                reply_serializer=ReplytSerializer(reply_query,many=True)
                comment['reply']=reply_serializer.data
                comment_data.append(comment)

            data.append(post)

        return Response(serialize.data)
#Post wrt Category
class PostCatView(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def get(self, request,cid=None):
        query=Post.objects.filter(category=cid)
        serialize=PostSerializer(query,many=True)
        data=[]
        for post in serialize.data:
            #######Likes
            post_like=Likes.objects.filter(post=post['id']).filter(like=True).count()
            ####checking me like or not
            myLikes=Likes.objects.filter(post=post['id']).filter(user=request.user).first()
            if myLikes:
                post['like']=myLikes.like
            else:
                post['like']=False
            post['totalLikes']=post_like
            #######Comments
            comment_query=Comment.objects.filter(post=post['id'])
            comment_serializer=CommentSerializer(comment_query,many=True)
            post['comment']=comment_serializer.data
            #######Reply
            comment_data=[]
            for comment in comment_serializer.data:
                reply_query=Reply.objects.filter(comment=comment['id'])
                reply_serializer=ReplytSerializer(reply_query,many=True)
                comment['reply']=reply_serializer.data
                comment_data.append(comment)

            data.append(post)

        return Response(serialize.data)


#Category Api
class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

#Category Api
# class ImageViewSet(viewsets.ModelViewSet):
#     queryset=ImageGet.objects.all()
#     serializer_class=ImageSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        dat={
            'username':request.data['username'],
            'email':request.data['email'],
            'password':request.data['password']
        }
        #img=request.data['image']
        #print(dat)
        serializer = self.get_serializer(data=dat)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #us=User.objects.filter('username'==request.data['username'] and 'email'==request.data['username'])
        # serializer_class = ProfileSerializer
        # def post(self, request, *args, **kwargs):
        #     print(request.data)
        #     dat={
                
        #         'image': img,
        #         'user': us
        #     }
        #     print(dat)
        #     serializer = self.get_serializer(data=dat)
        #     serializer.is_valid(raise_exception=True)
        #     user = serializer.save()
            
            

        #     print(us)
        #     return Response({
        #     "pic": "Uploaded"
        #     })

        

        #print(us)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
        