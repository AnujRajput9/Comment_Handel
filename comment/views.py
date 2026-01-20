from django.shortcuts import render ,get_list_or_404,redirect,get_object_or_404, redirect
from .models import Comment
from .forms import CommentForms , UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForms, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')

    default_comments = [
        {
            "user": "News",
            "image": "https://th-i.thgim.com/public/incoming/4is2dj/article70441195.ece/alternates/LANDSCAPE_1200/TH24-Koshy-EnviGQ0FBPICU.3.jpg.jpg",
            "text": (
                "The Aravalli Hills are one of the world's oldest fold mountain ranges, "
                "stretching across northwestern India (Delhi, Haryana, Rajasthan, Gujarat). "
                "They are vital for ecology, act as a natural barrier to desertification, "
                "and play an important role in water recharge. However, they are currently "
                "subject to controversy regarding their definition and protection from mining."
            ),
            "created_at": "Demo News"
        },
        {
            "user": "News",
            "image": "https://i.ytimg.com/vi/w4eTKHndETg/maxresdefault.jpg",
            "text": (
                "The NEET 2024 exam faced massive scam allegations involving question paper leaks "
                "and irregularities. The Supreme Court acknowledged limited impact and rejected "
                "calls for a complete re-exam, while the CBI continues its investigation."
            ),
            "created_at": "Demo News"
        }
    ]

    return render(
        request,
        "comment/comment_list.html",
        {
            "comments": comments,
            "default_comments": default_comments
        }
    )


 
# Create your views here.
def index(request):
    return render(request,'comment/index.html')

# /
# def comment_list(request):
#     comments = Comment.objects.all().order_by('-created_at')
#     return render(request,'comment/comment_list.html',{'comments':comments})

@login_required
def create_comment(request):
    if request.method == "POST":
        form =  CommentForms(request.POST,request.FILES) 
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  
            comment.save()
            return redirect('comment_list') 
    else:
        form = CommentForms()
    return render(request,'comment/create_comment.html',{'form':form}) 

@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == "POST":
        form = CommentForms(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            updated_comment = form.save(commit=False)
            updated_comment.user = request.user
            updated_comment.save()
            return redirect('comment_list')
    else:
        form = CommentForms(instance=comment)
    return render(request, 'comment/create_comment.html', {'form': form})


@login_required      
def delete_comment(request,comment_id):
    comment = get_object_or_404(Comment , pk= comment_id,user = request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment_list')
    return render(request,'comment/delete_comment.html',{'comment':comment}) 
               
               
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                login(request,user)
                return redirect('comment_list')
            except ValueError as e:
                print(e)
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})               
            