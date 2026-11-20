from django.shortcuts import render

# Create your views here.
from .serializers import page_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pages
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    
    return render(request,'home.html')

@login_required
def post(request):
    return render(request,'post.html')

@api_view(['GET'])
def pages_list(request):
    pages =Pages.objects.all()
    serializer =page_serializer(pages, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def pages_detail(request,pk):
    pages =Pages.objects.get(id=pk)
    serializer =page_serializer(pages,many =False)
    return Response(serializer.data)


@api_view(['POST'])
def page_post(request):
    print("1. page was called")
    print("2. request data:", request.data)

    serializer = page_serializer(data=request.data)

    valid = serializer.is_valid()

    print("3. valid:", valid)
    print("4. errors:", serializer.errors)

    if valid:
        pages = serializer.save(author=request.user)

        print("5. pages:", pages)
        print("6. id:", pages.id)
        print("7. serializer:", serializer.data)
        print("8. author:", pages.author)

        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['GET'])
def page_search(request):
    query =request.GET.get('q')
    if query:
        pages =Pages.objects.filter(title__icontains=query)
        serializer = page_serializer(pages,many=True)
        return Response(serializer.data)
    return Response({'message':'no query parameter provided'})




